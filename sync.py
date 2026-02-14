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
            print("❌ 无法解析文章标题，请检查链接是否为标准的微信文章")
            return
        title = title_tag.get_text(strip=True)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        content_area = soup.find('div', class_='rich_media_content')
        if not content_area:
            print("❌ 无法获取文章正文内容")
            return

        # 清理无用样式
        for tag in content_area.find_all(True):
            if tag.name not in ['img', 'video', 'iframe']:
                tag.attrs = {}

        # --- 3. 准备文件夹 (支持多级目录) ---
        # 核心修改：将 ID 中的 / 转换为系统路径斜杠，实现多级目录自动创建
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        img_dir = os.path.join(md_file_dir, IMAGE_SUBDIR)
        
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)
            print(f"📂 已创建目录: {img_dir}")

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
                    # 网页显示的相对路径：使用正斜杠 /
                    web_img_path = f"{IMAGE_SUBDIR}/{img_name}"
                    img.replace_with(f"\n\n![图片]({web_img_path})\n\n")
                except:
                    print(f"⚠️ 图片 {src} 下载失败")

        md_content = f"# {title}\n\n"
        md_content += f"> 发布日期: {date_str}\n\n"
        md_content += content_area.get_text(separator="\n\n")

        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📝 Markdown 已生成: {md_file_path}")

        # --- 5. 同步更新 index.html (精准插入逻辑) ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        # 检查是否重复
        if f"'{title}'" in index_content or f'\"{title}\"' in index_content:
            print(f"⚠️ 首页列表中已存在《{title}》，跳过插入。")
        else:
            # 网页访问路径统一用正斜杠
            md_path_web = f"articles/{category_id}/{safe_title}.md"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100, 999)}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_web}', date: '{date_str}' }},"
            
            # 核心修改：使用 re.escape 处理 category_id，使其支持 translated-work/reasoning 中的斜杠
            pattern = rf"(['\"]{re.escape(category_id)}['\"]\s*:\s*\[)"
            
            if re.search(pattern, index_content):
                index_content = re.sub(pattern, rf"\1\n            {new_entry}", index_content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                print(f"✅ 已将《{title}》成功同步至 index.html 的 {category_id} 分类")
            else:
                print(f"❌ 错误：在 index.html 中未找到分类标识 '{category_id}'，请检查 ID 是否完全一致")

    except Exception as e:
        print(f"💥 运行出错: {e}")

if __name__ == "__main__":
    download_and_sync()

