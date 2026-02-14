import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import random
from datetime import datetime

# --- 基础配置 ---
BASE_DIR = "articles" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== Actions Sync Start ===")
    
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip()
        print(f"URL: {url}")
        print(f"Category: {category_id}")
    else:
        print("Error: Missing arguments")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        title_tag = soup.find('h1', class_='rich_media_title') or soup.find('h1')
        title = title_tag.get_text().strip()
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        main_area = soup.find('div', id='js_content') or soup.find('div', class_='rich_media_content')
        
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        os.makedirs(md_file_dir, exist_ok=True)

        md_content = f"# {title}\n\n> {date_str}\n\n" + main_area.get_text(separator="\n\n")
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title).strip()
        
        with open(os.path.join(md_file_dir, f"{safe_title}.md"), 'w', encoding='utf-8') as f:
            f.write(md_content)

        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        if f"'{title}'" not in content and f'"{title}"' not in content:
            md_path = f"articles/{category_id}/{safe_title}.md"
            art_id = f"art_{datetime.now().strftime('%H%M%S')}"
            entry = f"{{ id: '{art_id}', title: '{title}', filePath: '{md_path}', date: '{date_str}' }},"
            
            # 使用最保守的匹配，不管引号还是空格
            # 只要 HTML 里有 category_id 就能找到
            target_pattern = rf"{re.escape(category_id)}['\"]\s*:\s*\["
            
            if re.search(target_pattern, content):
                content = re.sub(target_pattern, rf"{category_id}': [\n                {entry}", content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Success: Added to {category_id}")
            else:
                print(f"Error: Category {category_id} not found in HTML")
                sys.exit(1)
        else:
            print("Notice: Article already exists")

    except Exception as e:
        print(f"Crash: {e}")
        sys.exit(1)

# 直接运行，不再使用 if name == main 这种容易报错的结构
download_and_sync()
