import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import random
from datetime import datetime

# --- 基础配置 ---
BASE_DIR = "articles" 
IMAGE_SUBDIR = "images" 
VIDEO_SUBDIR = "videos" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园全自动更新：终极排版优化版 ===")
    
    # 1. 获取参数
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
        print(f"🔗 处理链接: {url}")
        print(f"📂 目标分类: {category_id}")
    else:
        print("❌ 错误：未接收到有效的文章链接")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # --- 2. 解析标题 ---
        title_tag = soup.find('h1', class_='rich_media_title')
        if not title_tag:
            print("❌ 无法解析文章标题")
            return
        title = title_tag.get_text(strip=True)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        content_area = soup.find('div', class_='rich_media_content')
        if not content_area:
            print("❌ 无法获取文章正文内容")
            return

        # --- 3. 准备文件夹 ---
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        img_dir = os.path.join(md_file_dir, IMAGE_SUBDIR)
        
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)

        # --- 4. 核心：精准正文清洗逻辑 (同时解决连成一片和句子断行) ---
        # 预处理：删除不需要的标签
        for s in content_area(['script', 'style', 'noscript']):
            s.decompose()

        lines = []
        # 遍历所有可能的段落标签
        for elem in content_area.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']):
            if elem.name == 'img':
                # 处理图片
                src = elem.get('data-src') or elem.get('src')
                if src:
                    img_count = len([f for f in os.listdir(img_dir) if f.startswith('img_')]) + 1
                    img_name = f"img_{img_count}.jpg"
                    img_path = os.path.join(img_dir, img_name)
                    try:
                        img_res = requests.get(src, headers=headers, timeout=10)
                        with open(img_path, 'wb') as f:
                            f.write(img_res.content)
                        # 插入图片 Markdown 语法
                        lines.append(f"![图片]({IMAGE_SUBDIR}/{img_name})")
                    except:
                        pass
                continue

            # 处理文本段落
            text = elem.get_text(strip=True)
            if not text:
                continue
            
            # 【核心修正 1】：消除文本内部的硬换行（解决句子断成两行的问题）
            clean_text = "".join(text.splitlines())
            
            # 【核心修正 2】：如果是标题，加上 Markdown 格式
            if elem.name.startswith('h'):
                lines.append(f"### {clean_text}")
            else:
                lines.append(clean_text)

        # 【核心修正 3】：段落之间统一用双换行连接（解决连成一片且控制间距）
        content_body = "\n\n".join(lines)

        md_content = f"# {title}\n\n> 发布日期: {date_str}\n\n{content_body}"

        # --- 5. 保存 Markdown ---
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📝 Markdown 已生成: {md_file_path}")

        # --- 6. 同步更新 index.html ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        if f"'{title}'" in index_content or f'\"{title}\"' in index_content:
            print(f"⚠️ 首页列表中已存在该文章，跳过插入。")
        else:
            md_path_web = f"articles/{category_id}/{safe_title}.md"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100, 999)}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_web}', date: '{date_str}' }},"
            
            pattern = rf"(['\"]{re.escape(category_id)}['\"]\s*:\s*\[)"
            if re.search(pattern, index_content):
                index_content = re.sub(pattern, rf"\1\n            {new_entry}", index_content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                print(f"✅ 已成功同步至 index.html")
            else:
                print(f"❌ 错误：在 index.html 中未找到分类标识 '{category_id}'")

    except Exception as e:
        print(f"💥 运行出错: {e}")

if __name__ == "__main__":
    download_and_sync()
