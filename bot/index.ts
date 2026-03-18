import { execSync } from "child_process";
import * as fs from "fs";
import * as path from "path";

// 分类对照表
const CATEGORIES: Record<number, string> = {
  1: "laochan-column",
  2: "ancient-greek",
  3: "metaphysics",
  4: "ethics",
  5: "epistemology",
  6: "logic",
  7: "aesthetics",
  8: "math-science-philosophy",
  9: "translated-work",
  10: "physics",
  11: "science",
  12: "technology",
  13: "ai",
  14: "religion",
  15: "economics",
  16: "law",
  17: "political",
  18: "social",
  19: "language",
  20: "existentialism",
  21: "phenomenology",
  22: "hermeneutics",
  23: "mind",
  24: "others",
};

const CATEGORY_MENU = `1.laochan-column  2.ancient-greek  3.metaphysics
4.ethics  5.epistemology  6.logic  7.aesthetics
8.math-science-philosophy  9.translated-work  10.physics
11.science  12.technology  13.ai  14.religion
15.economics  16.law  17.political  18.social
19.language  20.existentialism  21.phenomenology
22.hermeneutics  23.mind  24.others`;

const DATA_DIR = path.join(__dirname, "data");

// data 文件路径
const PUBLISHED_FILE = path.join(DATA_DIR, "published.json");
const PENDING_FILE = path.join(DATA_DIR, "pending.json");
const SESSION_FILE = path.join(DATA_DIR, "session.json");

// 确保 data 目录和文件存在
function ensureDataFiles() {
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }
  if (!fs.existsSync(PUBLISHED_FILE)) {
    fs.writeFileSync(PUBLISHED_FILE, JSON.stringify({ urls: [] }, null, 2));
  }
  if (!fs.existsSync(PENDING_FILE)) {
    fs.writeFileSync(PENDING_FILE, JSON.stringify({ articles: [] }, null, 2));
  }
  if (!fs.existsSync(SESSION_FILE)) {
    fs.writeFileSync(
      SESSION_FILE,
      JSON.stringify(
        { state: "waiting_select", selected: [], current_index: 0 },
        null,
        2
      )
    );
  }
}

function readJson<T>(filePath: string): T {
  return JSON.parse(fs.readFileSync(filePath, "utf-8")) as T;
}

function writeJson(filePath: string, data: unknown) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
}

// 读取 config.json
function loadConfig(): {
  rsshub_url: string;
  my_qq: string;
  github_repo: string;
  workflow_file: string;
  check_interval_minutes: number;
} {
  const configPath = path.join(__dirname, "config.json");
  return readJson(configPath);
}

// 解析 RSS XML，提取 title 和 link
function parseRss(xml: string): Array<{ title: string; url: string }> {
  const items: Array<{ title: string; url: string }> = [];
  const itemRegex = /<item>([\s\S]*?)<\/item>/g;
  let match;
  while ((match = itemRegex.exec(xml)) !== null) {
    const itemContent = match[1];
    const titleMatch = /<title><!\[CDATA\[(.*?)\]\]><\/title>|<title>(.*?)<\/title>/.exec(itemContent);
    const linkMatch = /<link>(.*?)<\/link>/.exec(itemContent);
    if (titleMatch && linkMatch) {
      const title = (titleMatch[1] || titleMatch[2] || "").trim();
      const url = linkMatch[1].trim();
      if (title && url) {
        items.push({ title, url });
      }
    }
  }
  return items;
}

// 功能一：定时检查（由 OpenClaw cron/scheduler 调用）
export async function onSchedule(ctx: { message: (qq: string, text: string) => void }) {
  ensureDataFiles();
  const config = loadConfig();

  // 获取 RSS
  let xml: string;
  try {
    const resp = await fetch(config.rsshub_url);
    xml = await resp.text();
  } catch (e) {
    console.error("RSS 获取失败:", e);
    return;
  }

  const articles = parseRss(xml);
  const published = readJson<{ urls: string[] }>(PUBLISHED_FILE);
  const pending = readJson<{ articles: Array<{ title: string; url: string }> }>(PENDING_FILE);

  const publishedSet = new Set(published.urls);
  const pendingUrls = new Set(pending.articles.map((a) => a.url));

  const newArticles = articles.filter(
    (a) => !publishedSet.has(a.url) && !pendingUrls.has(a.url)
  );

  if (newArticles.length === 0) return;

  // 追加到 pending.json
  pending.articles.push(...newArticles);
  writeJson(PENDING_FILE, pending);

  // 发私信通知
  const lines = newArticles.map((a, i) => `${i + 1}. 《${a.title}》`).join("\n");
  const msg = `📬 哲学园有 ${newArticles.length} 篇新文章：\n${lines}\n回复编号发布（如：1 3），或回复"跳过"`;
  ctx.message(config.my_qq, msg);
}

// 功能二：消息处理
export async function onMessage(ctx: {
  from: string;
  text: string;
  message: (qq: string, text: string) => void;
}) {
  ensureDataFiles();
  const config = loadConfig();

  // 只响应 my_qq 的私信
  if (ctx.from !== config.my_qq) return;

  const session = readJson<{
    state: "waiting_select" | "waiting_category";
    selected: Array<{ title: string; url: string }>;
    current_index: number;
  }>(SESSION_FILE);

  const text = ctx.text.trim();

  function reply(msg: string) {
    ctx.message(config.my_qq, msg);
  }

  function sendCategoryPrompt(article: { title: string; url: string }) {
    reply(`《${article.title}》选择分类：\n${CATEGORY_MENU}\n回复数字`);
  }

  if (session.state === "waiting_select") {
    if (text === "跳过") {
      writeJson(PENDING_FILE, { articles: [] });
      reply("已跳过本批文章");
      return;
    }

    // 尝试解析数字编号
    const nums = text.split(/\s+/).map(Number).filter((n) => !isNaN(n) && n > 0);
    if (nums.length === 0) {
      reply("请回复文章编号，如：1 3");
      return;
    }

    const pending = readJson<{ articles: Array<{ title: string; url: string }> }>(PENDING_FILE);
    const selected = nums
      .map((n) => pending.articles[n - 1])
      .filter(Boolean);

    if (selected.length === 0) {
      reply("请回复文章编号，如：1 3");
      return;
    }

    session.selected = selected;
    session.current_index = 0;
    session.state = "waiting_category";
    writeJson(SESSION_FILE, session);

    sendCategoryPrompt(selected[0]);
    return;
  }

  if (session.state === "waiting_category") {
    const num = parseInt(text, 10);
    if (isNaN(num) || num < 1 || num > 24) {
      reply("请回复 1-24 之间的数字");
      return;
    }

    const article = session.selected[session.current_index];
    const categoryId = num;
    const categoryName = CATEGORIES[categoryId];

    try {
      execSync(
        `gh workflow run ${config.workflow_file} --repo ${config.github_repo} -f article_url=${article.url} -f category_id=${categoryId}`,
        { stdio: "pipe" }
      );

      reply(`✅ 《${article.title}》已发布，分类：${categoryName}`);

      // 追加到 published.json
      const published = readJson<{ urls: string[] }>(PUBLISHED_FILE);
      published.urls.push(article.url);
      writeJson(PUBLISHED_FILE, published);

      // 从 pending.json 移除
      const pending = readJson<{ articles: Array<{ title: string; url: string }> }>(PENDING_FILE);
      pending.articles = pending.articles.filter((a) => a.url !== article.url);
      writeJson(PENDING_FILE, pending);
    } catch {
      reply(`❌ 《${article.title}》发布失败，请检查 gh auth 状态`);
    }

    session.current_index += 1;

    if (session.current_index >= session.selected.length) {
      writeJson(SESSION_FILE, {
        state: "waiting_select",
        selected: [],
        current_index: 0,
      });
      reply("🎉 本批处理完成");
    } else {
      writeJson(SESSION_FILE, session);
      sendCategoryPrompt(session.selected[session.current_index]);
    }
  }
}
