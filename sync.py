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

        # --- 2. 抓取标题 ---
        title_tag = soup.find('h1', class_='rich_media_title') or soup.find('h1')
        title = title_tag.get_text().strip() if title_tag else "未命名文章"
        # 移除非法文件名字符
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title).strip()
        # --- 2. 解析内容 ---
        title_tag = soup.find('h1', class_='rich_media_title')
        if not title_tag:
            print("❌ 无法解析文章标题，请检查链接是否为标准的微信文章")
            return
        title = title_tag.get_text(strip=True)
        date_str = datetime.now().strftime('%Y-%m-%d')

        # --- 3. 强化版正文定位 (解决开头段落丢失问题) ---
        main_area = soup.find('div', id='js_content') or \
                    soup.find('div', class_='rich_media_content')
        
        if not main_area:
            print("❌ 抓取失败：找不到文章正文区域。")
        content_area = soup.find('div', class_='rich_media_content')
        if not content_area:
            print("❌ 无法获取文章正文内容")
            return

        # 创建资源目录
        os.makedirs(os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title), exist_ok=True)
        # 清理无用样式
        for tag in content_area.find_all(True):
            if tag.name not in ['img', 'video', 'iframe']:
                tag.attrs = {}

        md_content = f"# {title}\n\n---\n\n"
        img_count = 0
        # --- 3. 准备文件夹 (支持多级目录) ---
        # 核心修改：将 ID 中的 / 转换为系统路径斜杠，实现多级目录自动创建
        category_path = category_id.replace('/', os.sep)
        md_file_dir = os.path.join(BASE_DIR, category_path)
        img_dir = os.path.join(md_file_dir, IMAGE_SUBDIR)

        # 遍历所有直接子元素，确保不漏掉任何 section 或 div 包裹的开头
        for element in main_area.find_all(True, recursive=False):
            # 处理图片
            all_imgs = element.find_all('img')
            for img in all_imgs:
                src = img.get('data-src') or img.get('src')
                if src and src.startswith('http'):
                    try:
                        img_res = requests.get(src, timeout=15)
                        if len(img_res.content) > 5000:
                            img_count += 1
                            img_name = f"{img_count}.jpg"
                            img_path = os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title, img_name)
                            with open(img_path, 'wb') as f:
                                f.write(img_res.content)
                            md_content += f"![图片](articles/images/{safe_title}/{img_name})\n\n"
                    except: pass
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)
            print(f"📂 已创建目录: {img_dir}")

            # 处理文字：使用 separator 确保嵌套文字不粘连
            text = element.get_text(separator="\n", strip=True)
            if text:
                if "扫描二维码" not in text and "阅读原文" not in text:
                    # 只有当块内文字不是纯图片占位符时才添加
                    if len(text) > 1 or not all_imgs:
                        md_content += f"{text}\n\n"
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

            # 处理视频占位
            html_str = str(element)
            if 'finder_video_card' in html_str or 'video' in html_str or element.find('iframe'):
                video_rel_path = f"articles/videos/{safe_title}/video.mp4"
                if video_rel_path not in md_content:
                    md_content += f'\n<div style="text-align:center;"><video src="{video_rel_path}" controls style="max-width:100%"></video></div>\n\n'
        md_content = f"# {title}\n\n"
        md_content += f"> 发布日期: {date_str}\n\n"
        md_content += content_area.get_text(separator="\n\n")

        # --- 4. 保存 Markdown 文件 ---
        md_file_dir = os.path.join(BASE_DIR, category_id)
        os.makedirs(md_file_dir, exist_ok=True)
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
        md_file_path = os.path.join(md_file_dir, f"{safe_title}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"📝 Markdown 已生成: {md_file_path}")

       # --- 5. 同步更新 index.html (精准插入逻辑) ---
        # --- 5. 同步更新 index.html (精准插入逻辑) ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        # 检查是否重复
        if f"'{title}'" in index_content or f'"{title}"' in index_content:
        if f"'{title}'" in index_content or f'\"{title}\"' in index_content:
            print(f"⚠️ 首页列表中已存在《{title}》，跳过插入。")
        else:
            # 网页访问路径统一用正斜杠
            md_path_web = f"articles/{category_id}/{safe_title}.md"
            # 生成唯一 ID
            article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100, 999)}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_web}', date: '{date_str}' }},"

            # 核心正则表达式：只找 [ 符号
            pattern = rf"(['\"]?{category_id}['\"]?\s*:\s*\[)"
            # 核心修改：使用 re.escape 处理 category_id，使其支持 translated-work/reasoning 中的斜杠
            pattern = rf"(['\"]{re.escape(category_id)}['\"]\s*:\s*\[)"

            if re.search(pattern, index_content):
                # 就在 [ 后面换行插入新内容，这样既不影响老文章，也能填满空括号
                index_content = re.sub(pattern, f"\\1\n                {new_entry}", index_content)
                
                # --- 5. 同步更新 index.html (最稳万能匹配逻辑) ---
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        # 核心正则：匹配 '分类名': [
        # 增加了 \s* 容错处理，并使用 re.IGNORECASE 忽略大小写
        pattern = rf"(['\"]?\s*{category_id}\s*['\"]?\s*:\s*\[)"
        
        if re.search(pattern, index_content, re.IGNORECASE):
            # 检查是否重复插入
            if f"'{title}'" in index_content or f'"{title}"' in index_content:
                print(f"⚠️ 首页列表中已存在《{title}》，跳过插入。")
            else:
                # 生成文章唯一 ID
                article_id = f"art_{datetime.now().strftime('%H%M%S')}{random.randint(100, 999)}"
                new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_web}', date: '{date_str}' }},"
                
                # 在匹配到的 [ 后面直接换行插入新内容
                index_content = re.sub(pattern, f"\\1\n                {new_entry}", index_content, flags=re.IGNORECASE)
                
                index_content = re.sub(pattern, rf"\1\n            {new_entry}", index_content)
                with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                    f.write(index_content)
                print(f"✅ 成功：文章已同步到 index.html 的 {category_id} 分类。")
        else:
            print(f"❌ 匹配失败：未在 index.html 中找到分类标识 '{category_id}': [")
            print("请检查 index.html 里的分类 ID 拼写是否与搬运选择的一致。")
                print(f"✅ 已将《{title}》成功同步至 index.html 的 {category_id} 分类")
            else:
                print(f"❌ 错误：在 index.html 中未找到分类标识 '{category_id}'，请检查 ID 是否完全一致")

    except Exception as e:
        print(f"❌ 运行中发生错误: {e}")
        print(f"💥 运行出错: {e}")

if __name__ == "__main__":
if __name__ == \"__main__\":
    download_and_sync()
