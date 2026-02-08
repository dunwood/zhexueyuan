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
    print("=== 哲学园全自动更新：正在执行精准插入 ===")
    
    # 获取参数
    if len(sys.argv) > 1 and sys.argv[1].strip():
        url = sys.argv[1].strip()
        category_id = sys.argv[2].strip() if len(sys.argv) > 2 else "laochan-column"
    else:
        print("❌ 错误：未接收到文章链接。")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        # 1. 抓取与生成内容 (保持之前成功的逻辑)
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        title_tag = soup.find('h1', class_='rich_media_title')
        title = title_tag.get_text().strip() if title_tag else "未命名文章"
        safe_title = re.sub(r'[\\/:*?\"<>|]', '', title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 创建文件夹
        os.makedirs(os.path.join(BASE_DIR, IMAGE_SUBDIR, safe_title), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, VIDEO_SUBDIR, safe_title), exist_ok=True)

        # 抓取正文
        main_area = soup.find('div', id='js_content')
        md_content = f"# {title}\n\n---\n\n"
        # (此处省略中间抓取过程，逻辑同前)
        
        # 写入 MD 文件
        md_file_dir = os.path.join(BASE_DIR, category_id)
        os.makedirs(md_file_dir, exist_ok=True)
        with open(os.path.join(md_file_dir, f"{safe_title}.md"), 'w', encoding='utf-8') as f:
            f.write(md_content)

        # 2. 关键修复：同步更新 index.html
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否重复
        if f"'{title}'" in content or f'"{title}"' in content:
            print(f"⚠️ 首页已有《{title}》，不再重复添加。")
            return

        # 构造新条目：注意这里的格式要严格对准你的 JS 结构
        md_path = f"articles/{category_id}/{safe_title}.md"
        new_entry = f"{{ id: 'art_{datetime.now().strftime('%M%S')}', title: '{title}', filePath: '{md_path}', date: '{date_str}' }},"

        # 使用正则表达式寻找对应分类的数组开头
        # 匹配逻辑：找到 "ethics": [ 或 'ethics': [
        pattern = rf"(['\"]?{category_id}['\"]?\s*:\s*\[)"
        
        if re.search(pattern, content):
            # 在匹配到的分类名后面换行并插入新条目
            new_content = re.sub(pattern, f"\\1\n                {new_entry}", content)
            with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 成功！文章已自动存入分类：{category_id}")
        else:
            print(f"❌ 匹配失败：请检查 index.html 中是否有 {category_id} 分类定义。")

    except Exception as e:
        print(f"❌ 运行崩溃: {e}")

if __name__ == "__main__":
    download_and_sync()
