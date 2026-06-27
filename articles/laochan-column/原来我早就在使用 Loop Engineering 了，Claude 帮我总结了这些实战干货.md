# 原来我早就在使用 Loop Engineering 了，Claude 帮我总结了这些实战干货

> 发布日期: 2026-06-27

![图片](/articles/images/原来我早就在使用 Loop Engineering 了，Claude 帮我总结了这些实战干货/img_2.jpg)

**老蝉问：**你知道Loop Engineering吧？

**CLAUDE思考：**识别概念并连接用户工作流程。 The user is asking in Chinese if I'm familiar with "Loop Engineering." I'm not immediately certain what they're referring to—it could be a company, a specific methodology, or something in the engineering or AI space. The phrasing suggests they expect me to know it, but I should acknowledge that "Loop Engineering" isn't a universally established term I can confidently speak to without more context. I'm not confident about what specific concept they're referring to, so rather than guess, I should search for "Loop Engineering" in an AI context to give them an accurate answer. I'll respond in Chinese since that's what they used.

Loop Engineering AI 概念 9 results

What Is Loop Engineering? The New Meta for AI Coding Agents | MindStudio www.mindstudio.ai

What Is Loop Engineering? The New Meta for Autonomous AI Agent Workflows | MindStudio www.mindstudio.ai

What Is Loop Engineering? AI Feedback Loops | Kilo kilo.ai

Loop Engineering: The Guide for AI Agents | Lushbinary lushbinary.com

Loop Engineering. The core of Loop Engineering | by Cobus Greyling | Jun, 2026 | Medium cobusgreyling.medium.com

AddyOsmani.com - Loop Engineering addyosmani.com

Loop Engineering cobusgreyling.substack.com

Loop Engineering：我們與 AI 協作方式的靜默革命 www.alphamatch.ai

The Art of Loop Engineering www.langchain.com 我理解了用户的背景和需求。现在我要用简洁直接的方式用中文解释 Loop Engineering，这个概念与他使用 Claude Code 和任务文件架构的工作流直接相关。

Done

**Claude回答：**知道。Loop Engineering（循环工程）是 2026 年 6 月前后兴起的一个概念，由 Google 工程师Addy Osmani推广，背后还有Peter Steinberger和 Anthropic Claude Code 负责人Boris Cherny的公开表态。

核心一句话：不再由你逐轮去提示 agent，而是去设计那个替你提示 agent 的系统。Boris Cherny 的原话大意是"我现在不提示 Claude 了，我写循环，循环去提示 Claude，决定该做什么"。

它和你已知概念的关系，按层级看：

**Prompt Engineering**—— 塑造单次输入

**Context / Harness Engineering**—— 装备单个 agent 运行的环境

**Loop Engineering**—— 坐在最上层，按计划去反复戳 agent、派生子 agent、自己喂自己

一个扎实的循环通常包含：触发器（timer / git 事件 / CI 信号）、目标（可验证的停止条件）、动作、观察、调整，外加一个记忆层。关键设计原则是 让一个独立的模型来判定"done"，而不是让干活的 agent 给自己打分——这样"完成"才有意义。

落到工具上：Claude Code 里对应 /loop、/schedule、/goal——跑到某个可验证条件满足为止；多 agent 并行时用 git worktree 做隔离，避免互相覆盖文件。

值得你警惕的三个风险（这几篇都反复强调）：

**Token 成本**会急剧攀升，无界限的自主循环烧钱很快,必须设最大迭代次数 / 最大运行时长。

**验证仍然是你的责任**。无人值守运行的循环，也是无人值守犯错的循环;"done"是一个声明,不是证明。

**理解债（comprehension debt）**。循环越快地交付你没写的代码,你实际理解的东西和仓库里存在的东西之间的差距就越大。

说实话，这个概念跟你现在的工作流高度重合——你已经在做 task 文件驱动 + CC 执行 + 真实运行产物验证。Loop Engineering 等于是把你这套"架构师/执行器/验证者"三角，往"让系统自己调度执行器、独立判定完成"的方向再推一层。你那条铁律"CC 自报完成不可信，只有真实运行的文件/日志/截图才算数"，正好对应这里说的"验证者子 agent 与执行者分离"。

你是想了解概念本身，还是在考虑把它引入到 media-forge / ModelHub 那套 CC 工作流里？

**老蝉问：**我是想先了解Loop Engineering的具体工作形态,然后再引入项目。你先介绍一下形态,比如说是跟我们以前task0x形式差不多,还是要一个控制台?还是要先写好一些通用的agent和skill?

**CLAUDE思考：**将用户现有工作流映射到循环工程的成熟度阶梯。 将用户现有工作流映射到循环工程的成熟度阶梯。 The user is asking about the practical implementation form of Loop Engineering—whether it operates like their current task0x setup, requires a console interface, or demands building general agents and skills beforehand. I need to find concrete operational details rather than just conceptual explanations to give them an accurate picture of what it actually looks like in practice.

Loop Engineering: The Guide for AI Agents | Lushbinary lushbinary.com

I'm looking at the three specific questions he's asking about his workflow with task files and Claude Code. The good news is that his existing task0x form is already most of the way there—it's about 90% aligned with what he needs.

The Ralph technique is essentially his manual task workflow automated into a loop: his task file becomes the spec, his verification step becomes the status tracking, and the difference is just automating the manual "press enter each round" part. For the console question, he doesn't need a custom dashboard—the built-in loop primitives in Claude Code or a simple bash while loop work fine, with memory stored in markdown files on disk. On skills and agents, he can start with just the minimal loop (spec file + state file + the loop itself) without needing to build general agents first, though skills will eventually help reduce repetitive context explanations.

I should be direct about what's concrete versus marketing framing—the technical foundations are solid and map to official docs, but the Ralph technique and building blocks are well-documented across multiple sources. His token cost concern is real, especially since he's using Claude Code as his executor already, so loop engineering on top of that is natural, but he'll want to watch the costs carefully.

Show less Done

**Claude回答：**先把结论给你：**Loop Engineering 的"形态"不是一个新控制台，而是把你现在的 task0x 流程外面套一层"自动按回车 + 自动判定完成"的壳**。你那套架构已经是它的手动版了。

下面分三层讲清楚形态。

### 一、最小形态：Ralph 技术（这就是你的 task0x + while 循环）

这个概念真正的起点叫**Ralph 技术**（Geoffrey Huntley 起的名，取自辛普森家族里那个"蠢得不像能用"的角色）。它的形态简单到就是一个 shell 循环：

对照你的工作流，几乎是一一对应的：

Ralph 形态

你现在的对应物

PLAN.md（spec / 任务清单）

你的 task01.md（项目全貌）+ taskXX.md

STATUS.md（外部状态文件）

你的验证产物 / 任务完成标记

每轮 fresh context

你那条/clear 清理上下文指令

你手动复制那行指令、按回车

关键洞察是**上下文重置**：长会话会随着窗口塞满旧推理、死胡同、过期文件内容而退化；Ralph 每一轮都是全新 agent、空白上下文，从磁盘读取仓库当前状态和任务清单，只做一个单元的工作，commit 后退出。智能不在某一次英雄式的长跑里，而在**清晰、颗粒化的规格 + 可验证的产出 + 模型污染不了的外部记忆**里——这正好是你"task 文件指定精确完成标准"那套铁律。

所以回答你第一个问题：跟 task0x 差不多，差的只是"谁按回车"。你是 Level 0（手动每轮），Loop Engineering 是把按回车这件事交给调度器。

### 二、需要控制台吗？

不需要自建控制台。"控制台"有两种现成形态，二选一：

**裸 while 循环 / cron**：上面那段 bash，或 Windows 任务计划程序定时触发。记忆全部落在磁盘的 markdown 文件，没有 UI。

**工具内置原语**：Claude Code 里/loop把你的节奏变成一个 cron job 并返回 job ID；/goal跨多轮一直跑到你写的条件被可验证地满足为止，而且每轮结束后由一个独立的、更小的模型判定是否完成——写代码的 agent 不是给自己打分的那个。

那个/goal原语是 2026 年讨论度最高的东西，因为它是"让循环自己决定结束、无需人在场"的关键件。注意：**这层会持续烧 token**——一个每轮都跑 verifier 的定时循环，开销可以飙得很快。以你 DeepSeek 为主力、对成本敏感的情况，第一个循环务必设死最多 N 轮 / $X 预算。

### 三、需要先写通用 agent 和 skill 吗？

**起步不需要，但往上爬时需要。**完整形态有"五大件 + 记忆"：

**Automations**（定时触发器，做发现和分类）

**Worktrees**（git worktree，让并行 agent 不互相覆盖文件)

**Skills**（把项目知识写下来，省得每轮重新解释）

**Connectors / MCP**（接到你真实的工具：issue、数据库、Slack）

**Sub-agents**（maker-checker 拆分：一个写、另一个查）

+**Memory**（磁盘上的 markdown / issue board，跨轮存"做完了什么、下一步什么"）

但你**不必一开始全做**。最小可跑的循环只要三样：spec 文件 + 状态文件 + while 循环。Skill 和 sub-agent 是你爬"成熟度阶梯"时逐级加的：

级别

循环做的事

人还在路径里吗

0 手动

你逐轮提示（**你现在在这**）

每一轮

1 分类

定时跑，把发现写进 markdown，不改代码

你读、你决定

2 草稿

在隔离 worktree 里起分支草拟修复

你审每个 PR

3 验证 PR

verifier sub-agent 先把关再到你

你批，verifier 过滤

4 自动合并

低风险类（依赖升级、lint、flaky 重试）绿了自动合

你审计日志，不审每个改动

**对你最关键的一件事**：第 5 件 sub-agent 的 maker-checker 拆分，本质就是你那条"CC 自报完成不可信，只有真实运行的文件/日志/截图才算数"的工程化版本——让一个独立模型对着 spec 和测试判定"done"，而不是干活的那个自己说完成了。你的验证纪律天然适配这个结构。

三个风险得提前知道（这几篇都反复敲）：验证责任永远在你（"done 是声明不是证明"）、理解债会更快累积（循环交付你没写的代码越快，仓库和你脑子里的差距越大）、以及"认知投降"（懒得有意见，循环给啥要啥）。

要不要我下一步基于你某个具体项目——比如 media-forge 的每日扫描，或 pdf-translate-agent 的批量翻译——给你设计一个**Level 1 的最小循环**（只做定时分类、不改代码、设死 token 上限），让你先安全地看它怎么跑，再决定往上爬？

**老蝉问：**好，你以media-forge设计一个Level 1 的最小循环。

**CLAUDE思考：**设计了媒体锻造的最小循环架构和验证流程。 设计了媒体锻造的最小循环架构和验证流程。 I'm thinking through what a Level 1 minimal loop for media-forge would look like—basically a scheduled task that runs periodically, gathers findings, and outputs them to a markdown file for human review and action, without making any code changes automatically. Let me recall the media-forge setup: it's running on localhost:3000 with Node.js and the DeepSeek API, has three main panels for daily scanning, writing, and tracking hot topics, and uses pipelines like runReview and runC.

The system already has cloud infrastructure on Cloudflare with Workers handling fetching, scanning, and radar duties via Cron scheduling, plus D1 and R2 for storage—the local side handles writing and translation. Since international RSS sources aren't accessible locally, the cloud component is essential. There's a note about verifying and potentially restarting those cloud Cron jobs since they stopped after June 11, and adding a scan-trigger interface to the cloud deployment pages.

For the Level 1 design, I need to account for the Windows environment constraints: PowerShell doesn't support && chaining, so I'll need separate commands; the run.bat plus manager.py pattern handles encoding and BOM/CRLF issues with Chinese text; server file changes require killing and restarting the process; and I can't trust self-reported completion—I need to verify by actually running files and checking logs. The approach should use universal mechanisms rather than patch fixes, maintain verification discipline, and be mindful of token costs.

Task files for new projects go in the project root, but media-forge's task files belong in D:\AI Project\media-forge\docs. The Level 1 loop itself should be a scheduled run that triggers the existing daily scan and radar functions, reads their raw output, triages and ranks topics by relevance to 哲学园 (the philosophy platform), groups them by theme with a one-line explanation of why each matters, and writes a prioritized findings list to a dated markdown file—essentially a daily topic triage report. This removes the manual chore of sifting through raw scan output to decide what's worth writing about, without actually generating articles or modifying code.

For the actual implementation, since media-forge already has cloud-based Cron and Workers running the scan and radar, the loop could be a scheduled local task (using Windows Task Scheduler) that calls the existing scan, pipes the output through a DeepSeek triage prompt, and writes the markdown findings file. The actual implementation for Level 1 is straightforward: a scheduled script that reads from the existing scan/radar endpoints, sends the raw output plus a triage rubric to DeepSeek, and writes the results to a markdown file while maintaining a state file to avoid re-triaging the same topics. At this level, it's really just a disciplined cron job rather than anything requiring agents or verification loops — the simplicity is the point.

For the runner itself, a standalone manager.py triggered via Task Scheduler fits his existing pattern best and keeps everything transparent and verifiable without touching the media-forge product code. The token cost is minimal since it's one API call per day over a batch, so I'd just set a hard cap on how many items get processed per run.

But there's a dependency I need to flag: the cloud scan Cron stopped after June 11, so the triage loop either needs to re-trigger the scan first or just work with whatever data's already sitting in D1/R2. I should design this cleanly with the rubric, the standalone manager setup, the three files it needs (spec, state tracking, output markdown), and the data flow from scan through triage to the final report.

I also need to cover the safety boundaries—read-only access, token limits, deduplication, no auto-publishing—plus how he'll verify it actually ran and when it's ready to hand off to Level 2. Since he wants the design first and prefers Claude.ai for architecture while CC handles execution, I should present the design and offer to turn it into a task file once he approves. I'm deciding whether a diagram is worth including—a data-flow loop showing the scan/radar feeding into triage, then the 简报, with the state file feeding back. His style is direct and concise, but a single clean diagram for system architecture isn't verbose and would genuinely help him visualize the feedback loop. I'll include one focused diagram of the media-forge loop anatomy.

Now let me sketch out the actual design spec: a daily scheduled job that takes raw output from runScan and the hotspot radar, classifies and ranks it by the philosophy garden's selection criteria, and produces a daily topic brief.

The system removes manual work — instead of manually reviewing raw scans and deciding what's worth writing, this script handles the initial filtering, grouping, and one-line reasoning, leaving only the selection step for the user. I'm implementing this as a standalone manager.py script triggered by Windows Task Scheduler daily, not as part of the console or CC loop, because the output is a markdown file that serves as the single source of truth.

The approach reads from existing media-forge outputs without touching product code, calls DeepSeek once daily for cost efficiency, and maintains three files: a rubric defining what makes a good topic, a JSON file tracking seen topics to prevent duplicates, and a daily markdown report with grouped and ranked selections.

The workflow runs on a schedule through a manager script that fetches raw entries, filters against the seen list, sends everything to DeepSeek for structured categorization, generates the daily report, updates the tracking file, and logs execution metrics—all while strictly adhering to read-only access on product data.

I'm setting hard limits on batch size (capping at 50 entries) and token budget per call, with failures stopping immediately and logged rather than retried to avoid wasted costs. The real validation comes from checking if the markdown report file actually appears in the directory and verifying the log contains timestamps, entry counts, and token usage—not trusting the script's self-reported success. One thing to note: the cloud Cron job stopped after June 11, so the pipeline depends on restoring that upstream data source first. 端扫描 Cron，要么让 manager.py 第 0 步先触发一次 scan。否则简报会是空的或陈旧的。

爬到 Level 2 的信号: 当简报连续一两周勾选率稳定、分类靠谱，你才考虑让它从"只筛"升到"筛完直接起草 E 类深度分析初稿到隔离分支"——但那是后话。

End: offer to turn this into docs/taskXX.md for CC.

Now, the dependency on cloud Cron stopped — I should mention but maybe I shouldn't over-assume. The memory says "stopped after June 11" and it's now June 24. So yes likely still stopped. Good to flag.

为了保持 Level 1 的最小化和安全性，直接消费现有输出更干净，但新鲜度需要上游保持活跃。我会把第 0 步定位为"确保上游数据新鲜：要么 cloud Cron 还在运行，要么 manager.py 先触发一次 scan"。最清晰的方案是让 manager.py 先调用 scan 端点（读路径，生成今天的数据），然后再做分类，这样整个流程就自洽了。触发 scan 本身不是代码改动，只是调用现有端点，写入 D1/R2 的行为也是既有的 scan 逻辑，对 Level 1 来说可以接受。

现在考虑是否值得画个图。他强调"直接简洁，不要冗长推理"，所以我得权衡一下——一个紧凑的数据流图（3 个文件 + 日循环 + 人工读取步骤）对架构师来说很有价值，但如果文字足够清楚就不必了。我倾向于先用文字规范，如果需要再补图。 A data-flow diagram will actually clarify the feedback loop better than prose alone, especially since he's evaluating the architecture. I'll include one compact diagram alongside tight text, then load the SVG module to build it with proper styling.

Writing SVG diagram...

Show less I'm sketching out a flowchart for the daily cycle that shows how the scheduler triggers manager.py to read the scan and radar files, feeds them into DeepSeek for triage, outputs to 简报.md, and then the human reviews it—with the state file and rubric as supporting inputs. I'll keep it to around five nodes in a horizontal flow layout. Building the SVG diagram... Now I'm laying out the vertical positions for each stage in the pipeline. The first stage is a scheduled trigger at y=40 with a two-line label showing the daily task scheduler. Then the raw entry fetching stage starts at y=116, followed by the DeepSeek classification stage at y=192, and the topic briefing generation stage beginning at y=268. I'm spacing each stage with gaps between them and calculating the exact y-coordinates so everything fits cleanly within the diagram. Positioning the arrows from the side inputs to stage 3, with the rubric arrow pointing to the upper portion and the seen arrow to the lower portion to avoid crossing. The viewBox needs to accommodate the lowest element at y=400 plus some buffer space.

Now I'm reconsidering whether the diagram actually adds value given the preference for conciseness, but I think a compact pipeline visualization is worth including for the architecture decision. I'll write out the SVG with proper classes and accessibility elements, being careful about text sizing—Chinese characters at 14px are roughly 15-18 pixels wide, so a title of about 14 characters should fit comfortably within the 240px box width. I'm settling on a color scheme for the pipeline: gray for the trigger and side inputs, blue for the read step, purple for the triage process, and teal for the output—keeping it to four distinct colors that each represent a different role in the workflow.

Writing component markup...

Show less Now I'm laying out the concrete design with the form choice, the three files, dataflow, boundaries, verification, dependency warning, and level-up signal—keeping it tight and focused. I'll wrap up by offering to write the taskXX.md file for the CC.

Done

**Claude回答：**好。media-forge 的 Level 1，本质是一个**选题分类循环**：每天定时把 runScan + 热点雷达的原始产出，按"哲学园选题价值"初筛分组，写成一份《每日选题简报》，**不写文章、不改任何 .js**。它替你干掉的那件重复活儿，就是你现在每天手动翻原始扫描结果、判断哪条值得写。

先看形态：## 形态选择：独立脚本 + 任务计划程序，不是控制台、不是 CC 循环

用你已有的**run.bat + manager.py**模式，Windows 任务计划程序每天定时拉起。理由三条，都贴你的铁律：

Level 1 要的是透明、产物即真相 —— 一个产出 markdown 的脚本，最符合你"只有真实运行的文件才算数"；

复用 run.bat + manager.py 解决中文 BOM/CRLF；

全程**只读**media-forge 已有产出，对产品代码零改动，符合 Level 1"no code changes"红线。

这一层**不需要 sub-agent、不需要 skill**。Ralph 的三件套就够：spec（rubric）+ state（seen）+ output（简报）。

### 三个文件

loop/rubric.md—— 选题价值规则。什么算好选题、哲学园调性、要排除什么。**这是你以后唯一需要手调的东西**，规则全写在这里，不写进代码。

loop/seen.json—— 状态/去重。已出现题目的指纹，防止同一个热点天天刷屏。

简报/选题简报-YYYY-MM-DD.md—— 产物。分组排序的选题清单，每条带一句"为什么值得写"+ 来源链接。

### 数据流（manager.py 一次运行）

拉取当日 scan + radar 原始条目（只读 D1/R2 或调只读接口）；

用seen.json滤掉重复题；

剩余条目 +rubric.md一次性喂 DeepSeek，要求输出固定结构（建议 JSON，再渲染成 markdown）；

写选题简报-日期.md；

更新seen.json；

追加一行运行日志：时间戳 + 处理条数 + token 消耗。

### Level 1 红线（写进任务文件的约束）

只读产品数据，绝不触发写作模块，绝不改任何.js；

硬上限：单次最多处理 N 条（建议 50），超出截断；

token 预算：调用设 max_tokens 上限并记录实际消耗；

失败即停 + 留日志，**不重试同一动作**（避免空转烧钱）。

### 验证标准（你怎么确认它真跑了）

不看脚本自报成功，看两样真实产物：当天简报/下出现新 markdown；运行日志里有时间戳 + 条数 + token。两样齐了才算这一轮成功。

### 一个依赖提醒

你的云端 Cron 6 月 11 之后停了。这个循环吃的是上游 scan/radar 的新鲜数据 —— 要么先恢复云端扫描 Cron，要么让manager.py第 0 步先主动触发一次 scan，否则简报会是空的或陈旧的。我建议第 0 步自触发，让循环自包含。

### 往 Level 2 爬的信号

当简报连续一两周**勾选率稳定、分类靠谱**，你才考虑升级:让它从"只筛"变成"筛完直接起草 E 类深度分析初稿到隔离分支"。在那之前不要动。

要我把这份设计落成一个D:\AI Project\media-forge\docs\下的 taskXX.md（含 rubric.md 初始规则模板、manager.py 接口约定、run.bat、验证清单）给 CC 执行吗？给你之前先确认一点：**简报里的"选题价值规则"，你想让我先起一版草稿，还是你口述几条核心标准我来成文？**

**老蝉问：**嗯，你上面写的是Level 1的具体执行过程。我现在是想要知道，我要做一个全新项目，形态上是否还是写设计书，然后出分解task？

**CLAUDE思考：**澄清了设计书与任务分解在循环工程中的核心地位。 澄清了设计书与任务分解在循环工程中的核心地位。 The user is asking whether Loop Engineering changes the fundamental authoring workflow itself, or if it still follows the same pattern of writing a design doc and decomposing it into tasks. This is a good distinction—they want to know if the front-end form of how they work with me changes, not just the mechanics of execution. Their current setup has me acting as architect in Claude.ai to generate task files, then Claude Code as executor reading those tasks, and they're wondering if adopting Loop Engineering would alter that basic structure.

The key realization is that Loop Engineering doesn't replace the design-and-decompose pattern—it actually makes that spec more central. The task files they're already creating become the durable plan that the loop reads and executes against, rather than them manually feeding each task to me one at a time. So the authoring form stays the same (design doc + task list), but the execution becomes automated: the loop reads the plan, picks the next unchecked task, runs it, verifies, marks it done, and repeats without their manual intervention between steps.

For new projects though, the maturity ladder matters—you don't jump straight to loops. You start by writing the design book and decomposing tasks first, then decide whether to drive them manually or wrap a loop around that same spec. The critical additions when adopting loops are a machine-readable status file that survives context resets, verifiable completion criteria per task (not vague prose but concrete checks like "tests pass" or "file exists"), and eventually the runner itself that orchestrates the whole cycle. The form stays the same — design book plus task decomposition remain the foundation, and they're actually more critical under the loop approach, not less. His existing artifacts map directly: the design book and task01 become the PLAN, the granular tasks become the task list, and what's added are three things: a machine-readable status file, per-task acceptance criteria, and a loop mechanism to iterate through them. 先手动跑一遍确认任务粒度没问题,再考虑自动化。关键的改变是完成判据必须能被机器检查——因为分工验证需要客观的评分标准。用简洁的文字说明现有产物如何映射到循环中的各个角色,避免过度格式化。

真正的差异在于任务的写法:现在可以依赖他读输出后主观判断,但循环就绪的任务必须自带验收测试,让检查者无需他参与就能判定完成。比如不是笼统的"实现搜索接口",而是"实现搜索接口;完成标准 = curl localhost:xxxx/search?q=test 返回 200 且 JSON 含 results 数组;禁止修改 writing 模块"。这其实就是他已经在做的"任务文件指定精确完成标准+约束"——只需把完成检查从文字变成可执行的形式。

Show less Done

**Claude回答：**是,形态不变 ——**设计书 + 分解 task 依然是地基**。Loop Engineering 不替换这一步,它坐在这一步**上面**。而且在循环里,这个地基比现在更重要,不是更轻。

原因很简单:Ralph 那套循环要的两样东西,你本来就在产出。

你现有的产物

在循环里的角色

设计书 / task01.md(项目全貌)

spec(PLAN)—— 每轮 fresh context 读的那份

分解的 taskXX.md

任务清单 —— 循环每轮"挑下一个未完成的"

所以你不用换一套新写法。真正的变化是**加三样、去一样**。

**加的三样:**

**一个机器可读的进度/状态文件**(STATUS.md 或带 checkbox 的清单)。这是上下文重置后唯一存活的记忆 —— agent 每轮都忘光,文件替它记"哪些做完了、下一个是哪个"。你现在靠脑子/对话记,循环里必须落盘。

**每个 task 的客观完成判据**。现在你可以写"实现搜索接口",因为你人在回路里、会读输出自己判断。循环里没人逐轮把关,判据必须是独立检查器能跑的东西 —— 不是"做好了",而是"curl localhost:xxxx/search返回 200 且 JSON 含 results 数组"。这正好是你那条"task 指定精确完成标准 + 什么不能改"铁律的工程化版,你已经走了八成,差的只是把 done 判据写成**可执行**的,而不是散文。

**(以后才加)一个 runner**—— 读任务清单、驱动 CC、判定、标记 done、重置、循环。这是你爬到 Level 2+ 才需要的东西。

**去的一样:**

你不再当那个"逐个复制 task、手动敲/clear 那行、按回车"的调度员。那一步 —— 也只有那一步 —— 交给循环。

**对全新项目的具体建议:别一上来就套循环。照旧先写设计书、分解 task**,但从第一天就把 task 写成"loop-ready":每个一个工作单元、带客观 done 判据、明确什么不能动。然后**先手动跑**(你现在的 Level 0)—— 用手动跑去验证你的 task 颗粒度对不对、判据够不够硬。等手动跑顺了、判据被证明是机器可判的,再考虑套壳自动化。

换句话说:循环不改变你**怎么写**,它改变的是写完之后**谁来逐轮喂**。把 task 的完成标准从"我看一眼就知道"升级成"一条命令就能判",你的整套 task0x 流程不用重写,就直接是 loop-ready 的。

**老蝉问：**如果再想减轻我的人工验证压力，要怎么做？原则是不能让CC自己验证。

**CLAUDE思考：**重构验证架构：机器检查+上游冻结+分层过滤。 重构验证架构：机器检查+上游冻结+分层过滤。 The core tension here is that the user wants to minimize manual verification work while maintaining an absolute rule: Claude can't verify its own outputs. Real verification means actually running the code, checking logs, taking screenshots, or hitting deployed endpoints—not just Claude claiming something works. I'm thinking through how to architect a system where verification gets offloaded to external, trustworthy sources rather than relying on Claude's self-assessment, and how to design tests that genuinely simulate real user behavior instead of just passing because Claude wrote both the code and the test. The real solution is shifting verification from subjective human judgment to deterministic, executable checks—scripts and tests that can't be gamed—and reserving LLM-based verification only for genuinely subjective parts where it's structured to avoid self-validation. This aligns with iwish's existing discipline of using automated verification scripts with clear pass/fail criteria, which is the strongest form of independence from CC's judgment. The key is that the verification script must be written separately from the implementation—ideally by the architect before any code exists—so the test becomes an external contract the implementation has to satisfy rather than something the code can be tailored to pass. This separation in authorship and timing prevents the executor from gaming the verification process.

For the parts that can't be made fully deterministic, like stylistic or translation fidelity checks, I need to rely on independence by construction: either using a different model to evaluate than the one that produced the work, or converting subjective criteria into objective proxies—like a linter that flags forbidden terms or patterns rather than relying on judgment calls.

The verifier should surface only failures to me, with the actual evidence (logs, diffs, assertions) attached, so I'm reading exceptions rather than every output. This tiered approach means the system gates quality before it reaches me, and my attention focuses on red flags plus spot-checks of passing items.

The verifier's evidence must be concrete artifacts—transcripts, exit codes, screenshots—not just claims of success, so even a pass is auditable. I can trust the automation but verify it through sampling: audit a percentage of auto-passed items, and if the sample stays clean, gradually trust it more. If something slips through, that's a signal to strengthen the deterministic checks rather than rely on the fallback.

The real insight is that verification has three tiers: what machines can check goes into automated tests upstream, what requires judgment but can be proxied goes to linters or evaluators, and what genuinely needs human judgment becomes just the failures and spot-checks. The way to reduce my load isn't to verify less—it's to verify earlier and by machine, moving the verification spec before implementation so it's executable and authored separately from whoever built it.

On the verifier sub-agent trap: the industry standard of splitting work between a maker and checker LLM doesn't actually satisfy the principle that CC can't verify itself if you're strict about it, since both are still LLMs. What iwish is pushing toward—deterministic, frozen verification—is actually stronger than what most loop-engineering approaches settle for, so I should encourage leaning into that discipline rather than defaulting to the weaker standard.

For concrete implementation across his projects: pdf-translate-agent already has a deterministic check script with 25+ assertions that fail at zero tolerance; media-forge treats completion as an API returning the expected shape plus passing a linter for forbidden terms and producing a factcheck report. For subjective quality like writing style, full automation is hard, so either bring in a different model to evaluate or keep human review but only sample-check. The real failure mode to watch for is teaching-to-the-test: if CC sees the verification script, it can overfit to pass those specific checks without solving the actual problem. Mitigations include hidden assertions that only run at verification time, keeping some checks out of CC's view. I'm weighing whether a diagram would help here—the three-tier verification model is really the structural answer to his question, and a clean visual could anchor it well. He prefers concision and I already used a diagram last turn, so I need to decide if it's worth the real estate. Given that this is an architecture decision and the layered verification funnel is the crux of the answer, I think one tight diagram is justified. I'm settling on prose-only to keep this tight and respect his preference for directness. The key reframe is that the bottleneck isn't verification itself but verification-by-reading—so the fix is catching issues earlier and letting machines handle the filtering. I'll structure around the independence hierarchy and flag that the loop-engineering approach (LLM verifier as sub-agent) sits in a weaker epistemic position. Writing this in Chinese to match his language. The key is making the verifier independent—authored separately and frozen before implementation, so it can't be gamed. I'd surface only failures to the user plus sample audits of passes, and when something slips through, promote that gap into a deterministic check. The pattern already exists in verify_output.py for pdf-translate-agent with FAIL=0; I should generalize that across every project, with each task shipping its verification script as part of the spec.

Show less Done

**Claude回答：**核心先说破:你现在的压力不是"在验证",而是**"在靠肉眼读着验证"**。减负的方向不是少验,而是**让验证尽量提前、并交给机器** —— 把"我读一眼判断"换成"一条命令跑出 pass/fail"。

而且要点醒你一句:Loop Engineering 圈子的标准答案(派一个 verifier sub-agent 来判/goal)其实**比你的原则弱**。那个 checker 还是个 LLM,还是能被"看起来做完了"糊弄过去。你"不能让 CC 自己验证"这条,逼着你走向更硬的路 ——**确定性验证**。这是对的,顺着它走。

### 验证独立性的三个梯度

谁来判

独立性

你的态度

同一个 CC、带着上下文说"done"

无(它给自己打分)

(你已经禁了)

另一个 fresh CC / 更强模型当 checker

弱(仍是 LLM 判断,可被说服)

仅用于无法确定性化的主观部分

(无 LLM)

强(机器不会被话术骗)

,能确定性化的全走这条

你 pdf-translate-agent 的verify_output.py(25+ 检查、FAIL=0)就是第三档的范本。减负的本质 =**把这个范本推广到每个项目、每个 task**。

### 让"机器验证"真正独立于 CC 的关键动作

光"写个验证脚本"不够 —— 如果验证脚本是 CC 自己写的,它会写一个自己代码刚好能过的测试(teach-to-the-test)。所以:

**判据由架构层(你 / Claude.ai)在出 task 时写,先于实现、且冻结。**验证脚本是 task spec 的一部分,不是执行器的产物。实现必须去满足一个它没权定义的外部标准。

**测行为/产出,不测"它做了哪些步骤"。**这正是你那条"测试要模拟真实用户、用户不知道被测的因果关系"原则 —— 对 CC 同样适用:验证它"curl /search返回 200 且 JSON 含 results 数组",而不是验证它"调用了搜索函数"。

**留一部分隐藏断言**(held-out),CC 看不到、只在验证时跑。等于给它一个它没法过拟合的测试集。

**验证器本身也守"无补丁"铁律**—— 不准针对特定输入写 if 特例,必须是对所有文档通用的检查。否则验证器自己就烂了。

做到这四条,"判分的"就不是 CC 了,是一份你预先写好、它改不动、机器执行的检查。这才叫没让它自己验。

### 主观部分(写作风格、翻译信达)怎么办

这块确实需要判断,但能**把判断降维成确定性代理**的尽量降:

你的forbidden_style.md→ 一个 linter,grep 出 Gödel/量子/海森堡之类禁词,命中即 FAIL。这是确定性的,不是 LLM。

风格 KPI → 可数指标(句长分布、禁用结构出现次数)。

真正剩下的纯主观(是不是老蝉味儿)→ 才动用"不同模型评判"或人工,且honest 设计:评判者不知道"标准答案",不引导。

### 你的实际负担:从"读全部"降到"读异常 + 抽检"

机器验证跑完,**绿的静默进"待用"堆,只有红的连同失败证据(日志/diff/失败断言)推到你面前**。你的注意力只花在:红的 + 对绿的做 N% 抽检。

抽检里漏掉一个坏的,说明你的测试有缺口 —— 这时把那一类失败**提升为新的确定性检查**(就是你"高频 fallback 必须固化成确定性代码"那条原则,用在验证上)。验证器越用越严,你抽检比例越降,负担单调下降。

一句话收口:**减负 = 把验证写在实现之前、用机器跑、由架构层冻结判据。**你不是少验,是把"读着验"换成"机器验完只给你看红灯"。你的verify_output.py已经证明这条路通了,缺的只是把它变成每个 task 的标配。

要不要我给你定一个**通用的 task 验证契约模板**—— 规定每个 taskXX.md 必须附带:可执行 done 判据、隐藏断言清单、产物清单(机器据此判 pass/fail)、以及哪些部分允许降级到人工抽检?有了这个模板,你之后所有新项目的 task 一出生就是"机器可验"的。

**老蝉问：**好，你出一个

**CLAUDE思考：**07:04

筹划创建中文结构化参考文档模板。 筹划创建中文结构化参考文档模板。 The user is asking for a universal task verification contract template that they can reuse across projects. This is a structured reference document they'll save and apply to future work, so it should be formatted as a reusable artifact. I need to verify whether the markdown skill exists before creating the file, though given how straightforward a template is, I'm confident a markdown file is the right format for this reusable contract specification. Let me start designing the verification contract template structure based on what we've discussed.

The template needs to capture the core elements: task boundaries and scope-creep prevention, executable acceptance criteria with actual commands rather than prose descriptions, a manifest of the real artifacts that count as truth, a frozen verification script convention, hidden assertions that Claude can't see during implementation, clear boundaries for where subjective judgment requires human spot-checking with defined sampling rates, universal verifier logic without special-case branching, explicit failure handling that stops and preserves evidence, and resource/token limits. I'll structure this as a tight, scannable template with fillable slots and a worked mini-example so he can see exactly how to apply it—no padding, every field justified, matching his preference for concision. Continuing to flesh out the template structure with scope boundaries that explicitly list what files and modules can be modified, what's off-limits, and forbidden actions to prevent scope creep. Then defining the deliverables checklist—the actual artifacts that will be executed or verified, whether that's files, logs, API responses, or screenshots—since self-reported completion doesn't count. Finally, I'm laying out the executable done criteria that the verify script will actually check against. 验证脚本需要遵循约定:退出码0表示通过,非0表示失败,且脚本内不能针对特定输入写特例,所有检查必须对全部输入通用。最后要识别这个任务中哪些判断点可以用linter或计数指标来确定性化,剩下的纯主观部分才需要人工评判。 I'm thinking through how to present this with enough granularity so he can see the concrete structure, and whether to keep the example inline or reference a file. Given his preference for minimal verbosity, I should probably show a compact filled example tied to the media-forge triage task we discussed, then ask how he wants to use it.

Show less

Check available public skills, including whether a markdown skill exists bash

ls /mnt/skills/public/ 2>/dev/null && echo "---" && ls /mnt/skills/public/md/ 2>/dev/null Output

docx

docx.skill

file-reading

file-reading.skill

frontend-design

frontend-design.skill

pdf

pdf-reading

pdf-reading.skill

pdf.skill

pptx

pptx.skill

product-self-knowledge

product-self-knowledge.skill

xlsx

### xlsx.skill

I'll create a markdown reference document with a structured template and example, keeping everything in Chinese as requested.

Done

Clude回答：没有专门的 md skill,这是纯结构化模板,直接写。模板出好了。结构是:三条铁律(判据先于实现并冻结、测产出不测步骤、真相只来自真实运行产物)+ 十个必填区块 + 一个用 media-forge 选题 task 填好的完整示例。

三个最吃劲的设计:**第 4 区隐藏断言**对 CC 屏蔽,防它写一个自己刚好能过的测试;**第 5 区无补丁红线**管住验证脚本本身不退化成特例堆;**第 7 区**把你的负担从"读全部"压到"看红灯 + 抽检",且抽检漏网就固化成新检查,负担单调下降。

你之后新项目出 task,照这个填,task 一出生就是机器可验的。等你定下某个项目要正式上,我可以帮你把它的verify.py和隐藏断言文件具体写出来 —— 那是这套契约里唯一需要逐项目定制的部分。

### Task 验证契约模板

用途:每个taskXX.md都内嵌本契约。目的是把"我读一眼判断"换成"一条命令跑出 pass/fail", 让验证提前、交给机器,并保证判分的不是 CC 自己。

### 三条铁律(贯穿全模板)

**判据先于实现、且冻结。**验证脚本与判据由架构层(你 / Claude.ai)在出 task 时写好,实现层(CC)不得修改。实现必须去满足一个它无权定义的外部标准。

**测产出/行为,不测步骤。**验证"接口返回了什么",不验证"它调了哪个函数"。CC 不知道被测的因果关系。

**真相只来自真实运行的产物。**文件 / 日志 / 部署 URL 响应 / 截图。CC 自报"已完成"一律无效。

### 模板正文(每个 taskXX.md 必含以下区块)

### 0. 任务标识

任务号 · 项目 · 绝对路径:

一句话目标:

### 1. 范围边界(硬约束,防越界)

允许改动:〔文件 / 模块清单〕

**禁止改动**:〔明确列出,例如*.js、写作模块、云端配置〕

禁止行为:〔例如触发写作、触发部署、改 schema〕

### 2. 产物清单(真相来源)

列出机器据以判定的真实产物,每条须可被独立打开 / 运行:

[ ] 文件:〔路径〕→ 期望特征〔存在 / 行数 / 含某字段〕

[ ] 日志:〔路径〕→ 期望字段〔时间戳 / 条数 / token〕

[ ] 接口:〔URL〕→ 期望响应〔状态码 / JSON 结构〕

[ ] 部署 / 截图:〔地址〕

### 3. 可执行 done 判据(公开,CC 可见)

不是散文,是命令。每条:命令→ 期望结果。

〔命令〕→ 〔期望:HTTP 200 / exit 0 / 输出含 X〕

〔命令〕→ 〔期望〕

判据只测行为与产出。

### 4. 隐藏断言(held-out,CC 不可见)

实现期间对 CC 屏蔽,仅验证时合入跑。防 teach-to-the-test 过拟合。

存放:单独文件,出 task 时**不**交给 CC。

内容:〔边界用例 / 异常输入 / 真实用户不会主动引导的场景〕

### 5. 验证脚本约定

脚本:verify.py(或等价),随 task 冻结,实现层不得改。

退出码:0= 全过,非0= 失败。

**无补丁红线**:脚本内禁止针对特定输入写if特例;每条检查必须对全部输入通用。

重跑前先杀旧进程 / 重启服务,防陈旧代码静默服务。

### 6. 主观部分降维(能确定性化的先确定性化)

逐条列出主观判断点及其降维方式:

〔风格 / 质量点〕 → 〔确定性代理:linter / 禁词 grep / 计数指标〕

真正剩下的纯主观 → 人工或独立模型评判;honest 设计:评判者不知标准答案、不被引导。

### 7. 人工介入边界(你实际花注意力的地方)

机器判 pass → 静默进"待用"堆,你抽检 **N%**。

机器判 fail → 连同失败证据(日志 / diff / 失败断言)推给你。

抽检发现漏网 → 把该类失败**提升为新的确定性检查**(固化),下次不再靠肉眼。

目标:抽检比例随固化单调下降。

### 8. 失败处理

任一判据 fail:停 + 留证据,**不重试同一动作**(避免空转烧钱)。

### 9. 资源上限

token / 轮次 / 时长 上限:〔数值〕

记录实际消耗到日志。

### 填写示例(media-forge 选题分类循环的一个 task)

### 0. 任务标识

task07 · media-forge ·D:\AI Project\media-forge\loop\

实现manager.py:拉取当日 scan+radar,按 rubric 初筛分类,写选题简报。

### 1. 范围边界

允许改动:loop/manager.py、loop/run.bat、loop/rubric.md、loop/seen.json

禁止改动:任何*.js、写作模块、云端 Worker 配置

禁止行为:不得触发写作管线、不得改 D1 schema

### 2. 产物清单

[ ] 文件:简报/选题简报-YYYY-MM-DD.md→ 当天存在,含 ≥1 个分组、每条带来源链接

[ ] 日志:loop/run.log→ 末行含 时间戳 + 处理条数 + token 数

[ ] 状态:loop/seen.json→ 运行后新增本次条目指纹

### 3. 可执行 done 判据

python loop/verify.py→ 末行打印FAIL=0

test -f "简报/选题简报-$(date +%F).md"→ exit 0

grep -c "来源" 简报/选题简报-*.md→ ≥1

### 4. 隐藏断言(CC 不可见,验证时合入)

喂入一组含 3 条重复题的构造数据 → 简报中该题只出现 1 次(去重生效)

喂入空 scan 结果 → 脚本正常退出且日志记处理条数=0,不崩溃

### 5. 验证脚本约定

loop/verify.py随本 task 冻结,CC 不得修改其判定逻辑

退出码 0/非0;无补丁红线;运行前taskkill旧 python 进程

### 6. 主观部分降维

"选题是否符合哲学园调性" → 降维为:命中rubric.md禁排清单的题 FAIL;其余进简报由你勾选,不在机器判定范围

### 7. 人工介入边界

简报生成 = pass → 你只读简报、勾选要写的(抽检不适用,这是产物消费)

verify FAIL → 推日志给你

若发现某类垃圾题反复入选 → 把该特征加进rubric.md禁排,固化

### 8. 失败处理

任一判据 fail:停,保留run.log与中间产物,不自动重跑

### 9. 资源上限

单次最多处理 50 条;DeepSeek 调用 max_tokens 设上限;实际 token 写入日志

### 一句话使用法

出 task 时,架构层填 0–9 全部区块并冻结verify.py与隐藏断言;CC 只读 0–3、5–6、8–9(看不到第 4 区);你只看红灯 + 抽检。

附录：

### 循环工程

Addy Osmani

2026 年 6 月 7 日

循环工程，就是把你自己从“提示 agent 的那个人”这个位置上替换掉。你设计一个系统，让它来替你做这件事。这里的 loop 可以被理解为一种递归目标：你定义一个目的，然后 AI 反复迭代，直到完成。我相信，这也许会成为我们与 coding agent 协作的未来方式。不过，现在仍然很早，我对此也保持怀疑，而且你绝对必须小心 token 成本（如果你 token 充裕或紧张，使用模式可能会有巨大差异），所以我想拆开讲讲它是什么，以及它意味着什么。

Peter Steinberger 最近说：“你不应该再提示 coding agents 了。你应该设计那些会提示你的 agents 的 loops。”类似地，Anthropic 的 Claude Code 负责人 Boris Cherny 说：“我不再提示 Claude 了。我有一些 loops 在运行，它们会提示 Claude，并弄清楚该做什么。我的工作是写 loops。”

好吧，那么这些到底是什么意思？

大概有两年时间，你要从一个 coding agent 那里得到东西，方法就是写一个好的 prompt，并给它足够的上下文。你输入一句话，读它返回的内容，再输入下一句话。agent 是一个工具，而你一直把它握在手里，一轮接一轮。这个阶段差不多结束了，或者至少有些人认为它将要结束。

现在，你构建一个小系统：它会发现工作，把工作分派出去，检查结果，写下哪些事情已经完成，然后决定下一步；你让这个系统去戳 agents，而不是由你自己去戳。我以前写过与此相近的东西，叫 agent harness engineering，也就是构建单个 agent 在其中运行的环境，以及 factory model——构建软件的系统。循环工程位于 harness 的上一层。它是 harness，但它按定时器运行，会生成小助手，并且会给自己喂料。

让我惊讶的是，这件事现在已经不太像是一个工具问题了。一年前，如果你想要一个 loop，你就得写一堆 bash，并且永远维护那堆东西；它是你的，而且只属于你。现在，这些部件已经内置在产品里了。Steinberger 的清单几乎可以一一映射到 Codex app 上，然后又几乎同样映射到 Claude Code 上。一旦你注意到二者的形状是一样的，你就不再争论到底用哪个工具；你只是设计一个 loop，让它无论你碰巧坐在哪个工具里都仍然有效。

### 五个部件，以及一些说明

一个 loop 需要五样东西，然后还需要一个用来记住事情的地方。我先把它们列出来，再做映射。

自动化：按计划触发，并且自己做发现和分诊。

worktrees：让两个并行工作的 agents 不会互相踩踏。

skills：写下项目知识，否则 agent 只会自己猜。

plugins 和 connectors：把 agent 接入你已经在使用的工具。

sub-agents：让一个 agent 产生想法，让另一个 agent 检查它。

然后是第六样东西：记忆。一个 markdown 文件，或者一个 Linear 看板，任何活在单次对话之外、保存“已经完成什么”和“下一步是什么”的东西。听起来蠢到不像重要事项。但这是每一个长时间运行的 agent 都依赖的同一个技巧；我在 long-running agents 里详细讲过它：模型在两次运行之间会忘掉一切，所以记忆必须在磁盘上，而不是在上下文里。agent 会忘，repo 不会。

现在这两个产品都已经拥有这五样东西。

原语

在 loop 中的作用

Codex app

Claude Code

Automations

按计划进行发现 + 分诊

Automations 标签页：选择项目、prompt、频率、环境；结果进入 Triage inbox；/goal用于一直运行直到完成

Scheduled tasks 和 cron、/loop、/goal、hooks、GitHub Actions

Worktrees

隔离并行功能开发

每个 thread 内置一个 worktree

、--worktree、隔离方式：subagent 上的 worktree

Skills

把项目知识编码下来

Agent Skills（SKILL.md），用$name调用，或隐式调用

Agent Skills（SKILL.md）

Plugins / connectors

连接你的工具

Connectors（MCP）加上用于分发的 plugins

MCP servers 加上 plugins

Sub-agents

构思与验证

在.codex/agents/中以 TOML 定义的 subagents

中的 task subagents，agent teams

State

追踪已经完成的事情

通过 connector 使用 Markdown 或 Linear

Markdown（AGENTS.md、progress files）或通过 MCP 使用 Linear

这些名称在不同地方略有差异，但能力本质上是同一个东西。让我逐一说明，因为老实说，细节正是一个 loop 能否稳住、还是悄悄到处漏水的关键。

### 自动化，这是心跳

自动化使一个 loop 成为真正的 loop，而不只是你曾经运行过一次的东西。在 Codex app 里，你在 Automations 标签页创建一个自动化，然后选择项目、它要运行的 prompt、运行频率，以及它是在你的本地 checkout 上运行，还是在后台 worktree 上运行。那些发现了东西的运行会进入 Triage inbox，而那些什么都没发现的运行会自己归档，这很不错。OpenAI 内部用它们处理一些无聊的事情，比如每日 issue 分诊、总结 CI 失败、撰写 commit briefings、寻找某人上周引入的 bug。而且，一个自动化可以调用一个 skill，所以你可以让这个周期性任务保持可维护：你触发$skill-name，而不是把一大堵指令粘进一个永远不会有人更新的 schedule 里。

Claude Code 通过调度和 hooks 到达同样的地方。你可以用/loop按间隔运行一个 prompt 或命令；你可以调度一个 cron task；你可以在 agent 生命周期的某些节点触发 shell commands；或者，如果你希望它在你合上笔记本之后仍继续运行，你可以把整件事推到 GitHub Actions。想法完全一样：你定义一个自治任务，给它一个节奏，然后发现结果会来到你这里，而不是由你到处去检查。

还有一个值得了解的会话内原语，它更接近本文真正讨论的东西。/loop按节奏重新运行。/goal则会一直运行，直到你写下的条件真正成立；而且在每一轮之后，一个单独的小模型会检查你是否已经完成，所以写代码的 agent 不是给自己打分的那一个。你可以给它类似这样的条件：“test/auth中的所有测试都通过，并且 lint 干净”，然后走开。Codex 也有同样的东西，也叫/goal，它会跨轮次持续工作，直到一个可验证的停止条件成立，并且支持暂停、恢复和清除。同一个原语，两个工具都有；这也正是整篇文章的模式。

所以，这一部分负责把工作浮现出来。loop 的其他部分则负责对这些工作采取行动。

### Worktrees，让并行不至于变成混乱

只要你运行不止一个 agent，文件就会开始相互碰撞，而这就会成为失败点。两个 agents 写同一个文件，和两个工程师同时提交同几行代码、而且此前没人互相沟通过，是完全一样的头疼问题。git worktree 可以修复这个问题：它是在自己分支上的一个独立工作目录，同时共享同一个 repo 历史，所以一个 agent 的编辑从字面上就碰不到另一个 agent 的 checkout。

Codex 把 worktree 支持直接内置进去，所以多个 threads 可以同时作用于同一个 repo，而不会相互撞上。Claude Code 通过git worktree、打开一个独立 checkout 会话的--worktree标志，以及你可以放在 subagent 上的isolation: worktree设置，给你同样的隔离；这样每个 helper 都会获得一个新的 checkout，并在完成后自己清理。我在 orchestration tax 里写过这一切的人类侧面：worktrees 消除了机械性的冲突，但你仍然是天花板。决定你实际能同时跑多少个 agent 的，是你的 review bandwidth，而不是工具本身。

### Skills，让你不再每次都解释自己的项目

skill 是一种方式，能让你停止像金鱼一样在每个 session 里重新解释同样的项目上下文。两个工具使用同样的格式：一个文件夹，里面有一个SKILL.md，保存指令和元数据，以及可选的脚本、参考资料、资产。Codex 会在你用$或/skills调用时运行一个 skill，也会在你的任务与 skill 描述匹配时自己运行它；这也是为什么一个紧凑、无聊的描述胜过一个聪明描述。Claude Code 也用同样方式做这件事，我在 agent skills 里写过这个模式。

skills 也是意图不再一次又一次向你收费的地方。我在 intent debt 中论证过，agent 每个 session 开始时都是冷启动的，它会用自信的猜测填补你意图中的任何空洞。skill 就是写在外部的意图：约定、构建步骤、“我们不这样做，是因为那次事故”，一次性写在 agent 每次运行都会读取的位置。没有 skills，loop 每个 cycle 都要从零重新推导你的整个项目；有了 skills，它就有点像在复利增长。

有一点要分清楚：skill 是 authoring format，而 plugin 是你分发它的方式。当你想在多个 repos 之间共享一个 skill，或者把几个 skills 打包在一起时，你把它们包装成 plugin。在 Codex 中如此，在 Claude Code 中也如此。

### Plugins 和 connectors，让 loop 触碰你的真实工具

一个只能看到文件系统的 loop，是一个很小的 loop。connectors 基于 MCP 构建，它们让 agent 可以读取你的 issue tracker、查询数据库、访问 staging api、在 Slack 里发一条消息。Codex 和 Claude Code 都能说 MCP，所以你为其中一个写的 connector 通常也能在另一个里直接工作。而 plugins 会把 connectors 和 skills 打包在一起，所以你的队友只需一次安装你的设置，而不用凭记忆重建整个东西。

这就是一个 agent 说“这是修复方案”和一个 loop 自己打开 PR、链接 Linear ticket，并在 CI 变绿后 ping 频道之间的差别。connectors 是 loop 能在你的真实环境里行动的原因，而不是只告诉你如果它能做的话它会做什么。

### Sub-agents，让制造者远离检查者

loop 中最有用的结构性东西，远远地，是把写东西的人和检查东西的人分开。写代码的模型在给自己的作业打分时太好说话了。另一个带着不同指令、有时甚至是不同模型的 agent，会抓住第一个 agent 自己说服自己接受的那些东西。

Codex 只有在你要求时才会生成 subagents，让它们同时运行，然后把结果折回到一个答案中。你可以在.codex/agents/里把自己的 agents 定义为 TOML 文件，每个文件都有 name、description、instructions，以及可选的 model 和 reasoning effort；这样你的安全 reviewer 可以是一个高 effort 的强模型，而你的 explorer 可以是某个快速、只读的东西。Claude Code 也用.claude/agents/里的 subagents 和可以在它们之间传递工作的 agent teams 做同样的事。两者中常见的拆分都是：一个 agent 探索，一个 agent 实现，一个 agent 按 spec 验证。

我已经两次提出过这个观点，一次是在 code agent orchestra 中，一次是在 adversarial code review 中。它在 loop 内部尤其重要的原因是：loop 会在你没看着的时候运行，所以一个你真正信任的 verifier，是你可以走开的唯一理由。subagents 确实会烧更多 token，因为每一个都会做自己的模型和工具工作，所以要把它们花在值得为第二意见付费的地方。这也基本上是 Claude Code 的/goal在底层所做的事情：由一个新的模型决定 loop 是否完成，而不是由做了这件事的那个模型来决定；制造者与检查者的分离，被应用到了停止条件本身。

### 一个 loop 看起来是什么样

把这些东西拼在一起，一个单独的 thread 就变成了一个小控制面板。下面是一种我一直在使用的形态。

每天早上，一个自动化在 repo 上运行。它的 prompt 调用一个 triage skill，这个 skill 会读取昨天的 CI 失败、open issues、recent commits，然后把发现写进一个 markdown 文件或 Linear 看板。对于每一个值得处理的发现，这个 thread 会打开一个隔离的 worktree，并派一个 sub-agent 起草修复方案，再派第二个 sub-agent 按照项目 skills 和现有测试审查这个草稿。

connectors 让这个 loop 能够打开 PR 并更新 ticket。任何 loop 自己处理不了的东西，都会进入 triage inbox，交给我。state file 是整件事的脊柱；它记住已经尝试过什么、什么通过了、什么仍然开放，所以明天早上的运行会从今天停止的地方继续。

看看你在那里实际做了什么。你只设计了一次。你没有提示这些步骤中的任何一个。这就是 Steinberger 的整个观点被落实成现实；而且无论在 Codex 还是 Claude Code 中，这都是同一个 loop，因为部件就是同样的部件。

### loop 仍然不会替你做什么

loop 改变了工作，但它并不会把你从工作中删除。而且随着 loop 变得更好，有三个问题实际上会变得更尖锐，而不是更容易。

验证仍然在你身上。一个无人看管运行的 loop，也是一个无人看管犯错的 loop。你把 verifier sub-agent 和 maker 分开的全部理由，就是让 loop 的“它完成了”有点意义；即便如此，“完成了”仍然是一个主张，而不是一个证明。我一直在重复 code review in the age of AI 里的同一句话：你的工作是交付你已经确认能工作的代码。

如果你允许，自己的理解仍然会腐烂。loop 越快地交付你没有写的代码，已经存在的东西与你实际理解的东西之间的差距就越大。那就是 comprehension debt，而一个顺滑的 loop 只会让它增长得更快，除非你阅读这个 loop 做出来的东西。

而舒服的姿态是危险的姿态。当 loop 自己运行时，你很容易停止拥有自己的判断，只是接受它给回来的东西。我把这叫作 cognitive surrender。当你带着判断力去做时，设计 loop 是解药；当你为了避免思考而做时，它就是加速剂。同一个动作，结果相反。

### 构建 loop。继续做工程师。

我认为，这是我们工作将如何演化的一次预演。话虽如此，如果我不亲自 review 代码，或者如果我完全依赖自动化 loops 来修复代码，我产品的质量就会受损。我很可能会陷入一个下行螺旋，不断把自己挖进一个更深的坑里。

话虽如此，尽管去设置你的 loops，但不要忘记，直接提示你的 agents 也同样有效。关键在于找到正确的平衡。

loops 也可能因为你这个人不同而产生不同结果。两个人可以构建完全相同的 loop，却得到完全相反的结果。一个人用它在自己深刻理解的工作上跑得更快。另一个人用它来避免理解工作本身。loop 不知道其中的区别。你知道。

这就是为什么 loop 设计比 prompt engineering 更难，而不是更容易。Cherny 的观点不是说工作变容易了，而是说杠杆点移动了。

构建 loop。但要像一个打算继续做工程师的人那样去构建它，而不只是像一个按下“开始”的人那样。