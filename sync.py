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
    print("=== 哲学园全自动更新：终极排版+黑体保留版 ===")
    
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

        # --- 2. 解析内容 ---
        title_tag = soup.find('h1', class_='rich_media_title')
        if not title_tag:
            print("❌ 无法解析文章标题")
            return
        title = title_tag.get_text(strip=True)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        content_area = soup.find('div', id='js_content') or soup.find('div', class_='rich_media_content')
        if not content_area:
            print("❌ 无法获取文章正文内容")
            return

        # --- 3. 准备文件夹 ---
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        img_dir = os.path.join(md_file_dir, IMAGE_SUBDIR)
        
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)

        # --- 4. 核心：精准正文清洗与黑体保留 ---
        # 预处理：删除不需要的干扰标签
        for s in content_area(['script', 'style', 'noscript']):
            s.decompose()

        lines = []
        # 遍历所有段落、标题和图片
        for elem in content_area.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']):
            # A. 处理图片
            if elem.name == 'img':
                src = elem.get('data-src') or elem.get('src')
                if src:
                    img_count = len([f for f in os.listdir(img_dir) if f.startswith('img_')]) + 1
                    img_name = f"img_{img_count}.jpg"
                    img_path = os.path.join(img_dir, img_name)
                    try:
                        img_res = requests.get(src, headers=headers, timeout=10)
                        with open(img_path, 'wb') as f:
                            f.write(img_res.content)
                        lines.append(f"![图片]({IMAGE_SUBDIR}/{img_name})")
                    except:
                        pass
                continue

            # B. 核心修改：保留黑体字 (将 strong/b 转换为 Markdown 加粗)
            for bold in elem.find_all(['strong', 'b']):
                b_text = bold.get_text(strip=True)
                if b_text:
                    # 在加粗符号前后加空格，确保 Markdown 解析稳定
                    bold.replace_with(f" **{b_text}** ")

            # C. 处理文本清洗
            text = elem.get_text(strip=True)
            if not text:
                continue
            
            # 【修正】：消除文本内部的硬换行（防止句子断开）
            clean_text = "".join(text.splitlines())
            
            # 【修正】：根据标签类型分配 Markdown 格式
            if elem.name.startswith('h'):
                lines.append(f"### {clean_text}")
            else:
                lines.append(clean_text)

        # 【修正】：段落间统一用双换行连接（防止连成一片，控制间距）
        content_body = "\n\n".join(lines)
        md_content = f"# {title}\n\n> 发布日期: {date_str}\n\n{content_body}"

        # --- 5. 保存 Markdown ---
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📝 Markdown 已生成: {md_file_path}")

        # --- 6. 同步更新 index.html ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f
