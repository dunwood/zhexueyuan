import requests
from bs4 import BeautifulSoup
import os
import re
import sys
from datetime import datetime

# --- 配置 ---
BASE_DIR = "articles" 
IMAGE_SUBDIR = "images" 
VIDEO_SUBDIR = "videos" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园全自动更新：增强内容提取版 ===")
    
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
        print(f"🔗 处理链接: {url}")
    else:
        print("❌ 错误：未接收到文章链接。")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. 抓取标题
        title_tag = soup.find('h1', class_='rich_media_title') or soup.find('h1')
        title = title_tag.get_text().strip() if title_tag else "未命名文章"
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 2. 定位正文（尝试多种可能的微信正文 ID）
        # 微信文章正文通常在 js_content 中，但也可能在其他地方
        main_area = soup.find('div', id='js_content') or \
                    soup.find('div', class_='rich_media_content') or \
                    soup.find('div', id='img-content')

        if not main_area:
            print("❌ 抓取失败：找不到文章正文区域。")
            return

        # 创建资源文件夹
        os.makedirs(os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title), exist_ok=True)

        md_content = f"# {title}\n\n---\n\n"
        img_count = 0
        
        # 3. 遍历提取内容
        # 使用 recursive=True 深度查找所有段落和元素
        for element in main_area.find_all(['p', 'section', 'img'], recursive=True):
            # 处理图片
            if element.name == 'img':
                src = element.get('data-src') or element.get('src')
                if src and src.startswith('http'):
                    try:
                        img_res = requests.get(src, timeout=10)
                        if len(img_res.content) > 5000:
                            img_count += 1
                            img_name = f"{img_count}.jpg"
                            with open(os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title, img_name), 'wb') as f:
                                f.write(img_res.content)
                            md_content += f"![图片](articles/images/{safe_title}/{img_name})\n\n"
                    except: pass
                continue

            # 处理视频标记 (探测视频组件)
            html_str = str(element)
            if 'finder_video_card' in html_str or 'video' in html_str:
                if 'video.mp4' not in md_content: # 避免重复标记
                    video_rel_path = f"articles/videos/{safe_title}/video.mp4"
                    md_content += f'\n<div style="text-align:center;"><video src="{video_rel_path}" controls style="max-width:100%"></video></div>\n\n'

            # 提取文本内容
            text = element.get_text(strip=True)
            if text and not element.find('img'):
                # 过滤掉一些微信自带的冗余提示
                if "扫描二维码" not in text and "阅读原文" not in text:
                    md_content += f"{text}\n\n"

        # 4. 保存文件与更新索引
        md_file_path = os.path.join(BASE_DIR, category_id, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ 内容已写入: {md_file_path}")

        # 更新 index.html (逻辑保持不变)
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        if f"'{title}'" not in content and f'"{title}"' not in content:
            md_path = f"articles/{category_id}/{safe_title}.md"
            new_entry = f"{{ id: 'art_{datetime.now().strftime('%M%S')}', title: '{title}', filePath: '{md_path}', date: '{date_str}' }},"
            pattern = rf"(['\"]?{category_id}['\"]?\s*:\s*\[)"
            if re.search(pattern, content):
                new_content = re.sub(pattern, f"\\1\n                {new_entry}", content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 首页索引已更新。")

    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    download_and_sync()
