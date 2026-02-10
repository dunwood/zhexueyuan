import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import random
from datetime import datetime

# --- 配置 ---
BASE_DIR = "articles" 
IMAGE_SUBDIR = "images" 
VIDEO_SUBDIR = "videos" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园同步系统：路径兼容优化版 ===")
    
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
    else:
        print("❌ 错误：未接收到文章链接。")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. 抓取标题并彻底清理特殊字符
        raw_title = soup.find('h1', class_='rich_media_title').get_text().strip()
        # 改进点：不仅移除 Windows 不允许的字符，还要移除引号、破折号等网页敏感字符
        safe_title = re.sub(r'[\\/:*?\"<>|“”‘’\s]', '', raw_title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 2. 创建目录
        img_dir = os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title)
        os.makedirs(img_dir, exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title), exist_ok=True)

        md_content = f"# {raw_title}\n\n---\n\n"
        img_count = 0
        
        main_area = soup.find('div', id='js_content')
        for element in main_area.find_all(True, recursive=False):
            # 处理图片：生成的路径不再包含引号
            all_imgs = element.find_all('img')
            for img in all_imgs:
                src = img.get('data-src') or img.get('src')
                if src and src.startswith('http'):
                    try:
                        img_res = requests.get(src, timeout=15)
                        if len(img_res.content) > 5000:
                            img_count += 1
                            img_name = f"{img_count}.jpg"
                            with open(os.path.join(img_dir, img_name), 'wb') as f:
                                f.write(img_res.content)
                            # 使用生成的安全标题构建路径
                            md_content += f"![图片](articles/images/{safe_title}/{img_name})\n\n"
                    except: pass

            text = element.get_text(separator="\n", strip=True)
            if text and "扫描二维码" not in text:
                if len(text) > 1 or not all_imgs:
                    md_content += f"{text}\n\n"

        # 3. 保存与索引更新 (逻辑同前，保持 ID 随机)
        md_file_path = os.path.join(BASE_DIR, category_id, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        if f"'{raw_title}'" not in content:
            article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100,999)}"
            new_entry = f"{{ id: '{article_id}', title: '{raw_title}', filePath: 'articles/{category_id}/{safe_title}.md', date: '{date_str}' }},"
            pattern = rf"(['\"]?{category_id}['\"]?\s*:\s*\[)"
            new_content = re.sub(pattern, f"\\1\n                {new_entry}", content)
            with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                f.write(new_content)
        print(f"✅ 同步成功！清理后的安全文件夹名为: {safe_title}")

    except Exception as e:
        print(f"❌ 运行崩溃: {e}")

if __name__ == "__main__":
    download_and_sync()
