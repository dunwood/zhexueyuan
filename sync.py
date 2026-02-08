import requests
from bs4 import BeautifulSoup
import os
import re
import sys  # 【新增：用于读取外部参数】
from datetime import datetime

# --- 规范化路径配置 ---
BASE_DIR = "articles" 
IMAGE_SUBDIR = "images" 
VIDEO_SUBDIR = "videos" 
INDEX_FILE = "index.html" 

def download_and_sync():
    print("=== 哲学园一键同步 (GitHub Actions 云端适配版) ===")
    
    # --- 修改输入逻辑：优先读取外部参数，没有则手动输入 ---
    if len(sys.argv) > 1:
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
        print(f"🔗 正在处理链接: {url}")
        print(f"📁 目标分类: {category_id}")
    else:
        url = input("请输入微信文章链接: ").strip()
        if not url: return
        print("\n请选择文章分类: [1]老蝉专栏 [2]古希腊 [3]形而上学 ...")
        cat_map = {"1":"laochan-column", "2":"ancient-greek", "3":"metaphysics", "4":"ethics", "5":"epistemology", "6":"logic", "7":"aesthetics", "8":"math-science-philosophy"}
        category_id = cat_map.get(input("请输入编号 (默认'1'): ").strip(), "laochan-column")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. 标题处理
        title_tag = soup.find('h1', class_='rich_media_title')
        title = title_tag.get_text().strip() if title_tag else "未命名"
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 创建文件夹坑位
        local_img_dir = os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title)
        os.makedirs(local_img_dir, exist_ok=True)
        local_video_dir = os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title)
        os.makedirs(local_video_dir, exist_ok=True)

        # 2. 正文抓取 (保留原始逻辑)
        main_area = soup.find('div', id='js_content')
        md_content = f"# {title}\n\n---\n\n"
        img_count = 0
        
        for element in main_area.children:
            if isinstance(element, str):
                if element.strip(): md_content += f"{element.strip()}\n\n"
                continue
            if element.find_all('img') or element.name == 'img':
                imgs = element.find_all('img') if element.name != 'img' else [element]
                for img in imgs:
                    src = img.get('data-src') or img.get('src')
                    if src and 'wx_fmt=gif' not in src:
                        try:
                            img_res = requests.get(src, headers={'Referer': 'https://mp.weixin.qq.com/'}, timeout=10)
                            if len(img_res.content) > 5000:
                                img_count += 1
                                img_name = f"{img_count}.jpg"
                                with open(os.path.join(local_img_dir, img_name), 'wb') as f: f.write(img_res.content)
                                md_content += f"![图片](articles/images/{safe_title}/{img_name})\n\n"
                        except: continue
            
            # 处理视频嵌入标签
            html_str = str(element)
            if 'finder_video_card' in html_str or element.find('iframe') or 'video' in html_str:
                video_rel_path = f"articles/videos/{safe_title}/video.mp4"
                video_tag = f'\n<div style="text-align:center;"><video src="{video_rel_path}" controls style="max-width:100%"></video></div>\n'
                if video_tag not in md_content: md_content += video_tag

            text = element.get_text(strip=True)
            if text and not element.find('img'): md_content += f"{text}\n\n"

        # 3. 保存 MD 文件
        md_file_dir = os.path.join(BASE_DIR, category_id)
        os.makedirs(md_file_dir, exist_ok=True)
        md_file_name = f"{safe_title}.md"
        with open(os.path.join(md_file_dir, md_file_name), 'w', encoding='utf-8') as f: f.write(md_content)

        # 4. 同步 index.html
        with open(INDEX_FILE, 'r', encoding='utf-8') as f: index_content = f.read()
        if f"'{title}'" in index_content or f'"{title}"' in index_content:
            print(f"⚠️ 首页已存在《{title}》")
        else:
            md_path_for_index = f"articles/{category_id}/{md_file_name}"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_for_index}', date: '{date_str}' }},"
            pattern = rf"(['\"]{category_id}['\"]:\s*\[)"
            index_content = re.sub(pattern, f"\\1\n                {new_entry}", index_content)
            with open(INDEX_FILE, 'w', encoding='utf-8') as f: f.write(index_content)
            print(f"✅ 更新成功。")

    except Exception as e:
        print(f"❌ 出错: {e}")

if __name__ == "__main__":
    download_and_sync()