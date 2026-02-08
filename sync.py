import requests
from bs4 import BeautifulSoup
import os
import re
import sys
from datetime import datetime

# --- 基础配置 ---
BASE_DIR = "articles" 
IMAGE_SUBDIR = "images" 
VIDEO_SUBDIR = "videos" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园全自动同步系统 (增强版) ===")
    
    # 1. 读取参数：优先读取 GitHub Actions 传来的分类和链接
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        # 如果下拉菜单传来了分类 ID，就用它；否则默认老蝉专栏
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
        print(f"🔗 正在处理链接: {url}")
        print(f"📂 目标分类 ID: {category_id}")
    else:
        print("❌ 错误：未接收到有效的文章链接。")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # --- 抓取标题 ---
        title_tag = soup.find('h1', class_='rich_media_title')
        title = title_tag.get_text().strip() if title_tag else "未命名文章"
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # --- 创建文件夹坑位 ---
        os.makedirs(os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title), exist_ok=True)
        print(f"📁 文件夹已就绪: {safe_title}")

        # --- 正文处理逻辑 ---
        main_area = soup.find('div', id='js_content')
        md_content = f"# {title}\n\n---\n\n"
        img_count = 0
        
        for element in main_area.children:
            if isinstance(element, str):
                if element.strip(): md_content += f"{element.strip()}\n\n"
                continue
            
            # 处理图片
            if element.find_all('img') or element.name == 'img':
                imgs = element.find_all('img') if element.name != 'img' else [element]
                for img in imgs:
                    src = img.get('data-src') or img.get('src')
                    if src:
                        try:
                            img_res = requests.get(src, timeout=10)
                            if len(img_res.content) > 5000:
                                img_count += 1
                                img_name = f"{img_count}.jpg"
                                img_path = os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title, img_name)
                                with open(img_path, 'wb') as f: f.write(img_res.content)
                                md_content += f"![图片](articles/images/{safe_title}/{img_name})\n\n"
                        except: continue
            
            # 标记视频位置
            html_str = str(element)
            if 'finder_video_card' in html_str or element.find('iframe') or 'video' in html_str:
                video_rel_path = f"articles/videos/{safe_title}/video.mp4"
                md_content += f'\n<div style="text-align:center;"><video src="{video_rel_path}" controls style="max-width:100%"></video></div>\n'

            # 提取文本
            text = element.get_text(strip=True)
            if text and not element.find('img'): md_content += f"{text}\n\n"

        # --- 保存 Markdown 文件 ---
        md_file_dir = os.path.join(BASE_DIR, category_id)
        os.makedirs(md_file_dir, exist_ok=True)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📝 Markdown 已生成: {md_file_path}")

        # --- 核心：同步更新 index.html ---
        if not os.path.exists(INDEX_FILE):
            print(f"❌ 找不到 {INDEX_FILE}")
            return

        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        # 检查是否重复
        if f"'{title}'" in index_content or f'"{title}"' in index_content:
            print(f"⚠️ 首页列表中已存在《{title}》，跳过插入。")
        else:
            md_path_for_web = f"articles/{category_id}/{safe_title}.md"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_for_web}', date: '{date_str}' }},"
            
            # 正则表达式说明：匹配 "分类名": [ 或 '分类名': [，不论空格多少
            pattern = rf"(['\"]{category_id}['\"]\s*:\s*\[)"
            
            if re.search(pattern, index_content):
                # 在找到的标志后面插入新条目
                index_content = re.sub(pattern, f"\\1\n                {new_entry}", index_content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                print(f"✅ 首页 index.html 已成功更新，文章已归类至: {category_id}")
            else:
                print(f"❌ 匹配失败：在 index.html 中没找到 '{category_id}': [ 的标志。")
                print("💡 请检查 index.html 里的分类 ID 是否与下拉菜单中的 ID 完全一致。")

    except Exception as e:
        print(f"❌ 运行中发生崩溃: {e}")

if __name__ == "__main__":
    download_and_sync()
