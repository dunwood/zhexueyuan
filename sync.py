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
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园全自动更新：终极兼容版 ===")
    
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
        
        content_area = soup.find('div', class_='rich_media_content')
        if not content_area:
            print("❌ 无法获取文章正文内容")
            return

        # 清理样式
        for tag in content_area.find_all(True):
            if tag.name not in ['img', 'video', 'iframe']:
                tag.attrs = {}

        # --- 3. 准备文件夹 ---
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        img_dir = os.path.join(md_file_dir, IMAGE_SUBDIR)
        
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)

        # --- 4. 处理图片并生成 Markdown ---
        img_count = 0
        for img in content_area.find_all('img'):
            src = img.get('data-src') or img.get('src')
            if src:
                img_count += 1
                img_name = f"img_{img_count}.jpg"
                img_path = os.path.join(img_dir, img_name)
                try:
                    img_res = requests.get(src, headers=headers)
                    with open(img_path, 'wb') as f:
                        f.write(img_res.content)
                    web_img_path = f"{IMAGE_SUBDIR}/{img_name}"
                    img.replace_with(f"\n\n![图片]({web_img_path})\n\n")
                except:
                    pass

        md_content = f"# {title}\n\n> 发布日期: {date_str}\n\n" + content_area.get_text(separator="\n\n")
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # --- 5. 同步更新 index.html ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        if f"'{title}'" in index_content or f'"{title}"' in index_content:
            print(f"⚠️ 首页列表中已存在《{title}》，跳过。")
        else:
            md_path_web = f"articles/{category_id}/{safe_title}.md"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100, 999)}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_web}', date: '{date_str}' }},"
            
            # 使用 re.escape 确保带斜杠的 ID（如 translated-work/reasoning）能被搜索到
            pattern = rf"(['\"]{re.escape(category_id)}['\"]\s*:\s*\[)"
            
            if re.search(pattern, index_content):
                # 插入到数组的第一行
                index_content = re.sub(pattern, rf"\1\n                {new_entry}", index_content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                print(f"✅ 已成功同步到分类: {category_id}")
            else:
                print(f"❌ 错误：index.html 中找不到标识 '{category_id}'")
                sys.exit(1)

    except Exception as e:
        print(f"💥 运行出错: {e}")
        sys.exit(1)

# 注意：这里修正了之前报错的转义问题
if __name__ == "__main__":
    download_and_sync()
