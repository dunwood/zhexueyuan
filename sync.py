import requests
from bs4 import BeautifulSoup
import os
import re
import subprocess
from datetime import datetime
import time
import json
import sys

# --- 规范化路径配置 ---
BASE_DIR = "articles"
IMAGE_SUBDIR = "images"
INDEX_FILE = "index.html"
LINKS_FILE = "links.txt"
LOG_FILE = "sync.log"

# --- 文章分类映射 ---
CAT_MAP = {
    "1": "laochan-column",
    "2": "ancient-greek",
    "3": "metaphysics",
    "4": "ethics",
    "5": "epistemology",
    "6": "logic",
    "7": "aesthetics",
    "8": "math-science-philosophy"
}

CAT_NAMES = {
    "laochan-column": "老蝉专栏",
    "ancient-greek": "古希腊哲学",
    "metaphysics": "形而上学",
    "ethics": "伦理学",
    "epistemology": "认识论",
    "logic": "逻辑学",
    "aesthetics": "美学",
    "math-science-philosophy": "数理、科哲"
}

def log(message):
    """记录日志到文件和控制台"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] {message}"
    print(log_message)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_message + '\n')

def is_git_repo():
    """检查当前目录是否是git仓库"""
    return os.path.exists('.git')

def git_push():
    """自动推送到GitHub"""
    if not is_git_repo():
        log("[警告] 当前目录不是Git仓库，跳过推送")
        return False
    
    try:
        # 检查是否有变更
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            log("[信息] 没有新的变更需要提交")
            return True
        
        # 添加所有变更
        log("[添加] 正在添加文件到Git...")
        subprocess.run(['git', 'add', '.'], check=True)
        
        # 提交
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        commit_msg = f"自动同步文章 - {timestamp}"
        log(f"[保存] 正在提交: {commit_msg}")
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        
        # 推送
        log("[推送] 正在推送到GitHub...")
        subprocess.run(['git', 'push'], check=True)
        
        log("[成功] GitHub推送成功！")
        return True
        
    except subprocess.CalledProcessError as e:
        log(f"[错误] Git操作失败: {e}")
        return False
    except Exception as e:
        log(f"[错误] 推送出错: {e}")
        return False

def download_article(url, category_id="laochan-column"):
    """下载单个文章"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        log(f"[下载] 正在下载: {url}")
        res = requests.get(url, headers=headers, timeout=30)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. 标题处理
        title_tag = soup.find('h1', class_='rich_media_title')
        title = title_tag.get_text().strip() if title_tag else "未命名"
        safe_title = re.sub(r'[\\/:*?"<>|]', '', title)
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 图片专属文件夹
        img_folder_name = safe_title
        local_img_dir = os.path.join(BASE_DIR, IMAGE_SUBDIR, img_folder_name)
        os.makedirs(local_img_dir, exist_ok=True)

        # 2. 定位正文
        main_area = soup.find('div', id='js_content')
        if not main_area:
            log(f"[错误] 无法抓取正文: {title}")
            return False

        md_content = f"# {title}\n\n---\n\n"
        img_count = 0
        
        # 3. 递归遍历所有元素
        for element in main_area.children:
            if isinstance(element, str):
                if element.strip():
                    md_content += f"{element.strip()}\n\n"
                continue

            # A. 处理图片
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
                                with open(os.path.join(local_img_dir, img_name), 'wb') as f:
                                    f.write(img_res.content)
                                md_img_path = f"articles/images/{img_folder_name}/{img_name}"
                                md_content += f"![图片]({md_img_path})\n\n"
                        except Exception as e:
                            log(f"[警告] 图片下载失败: {e}")
                            continue
            
            # B. 处理视频
            html_str = str(element)
            if 'finder_video_card' in html_str or element.find('iframe') or 'video' in html_str:
                video_note = "【[视频] 此处原文章有一条视频，因版权限制无法同步，请点击文末'阅读原文'查看】"
                if video_note not in md_content:
                    md_content += f"\n> {video_note}\n\n"

            # C. 处理文本
            text = element.get_text(strip=True)
            if text and not element.find('img'):
                md_content += f"{text}\n\n"

        # 4. 保存 MD
        md_file_dir = os.path.join(BASE_DIR, category_id)
        os.makedirs(md_file_dir, exist_ok=True)
        md_file_name = f"{safe_title}.md"
        md_file_path = os.path.join(md_file_dir, md_file_name)
        
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # 5. 同步 index.html
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_content = f.read()

        if f"'{title}'" in index_content or f'"{title}"' in index_content:
            log(f"[警告] 首页已存在《{title}》，仅更新本地文件。")
        else:
            md_path_for_index = f"articles/{category_id}/{md_file_name}"
            article_id = f"art_{datetime.now().strftime('%H%M%S')}"
            new_entry = f"{{ id: '{article_id}', title: '{title}', filePath: '{md_path_for_index}', date: '{date_str}' }},"
            pattern = rf"(['\"]{category_id}['\"]:\s*\[)"
            index_content = re.sub(pattern, f"\\1\n                {new_entry}", index_content)
            with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                f.write(index_content)
            log(f"[成功] 首页 index.html 已更新")

        log(f"[成功] 文章《{title}》处理完成，共{img_count}张图片")
        return True

    except Exception as e:
        log(f"[错误] 处理文章失败 ({url}): {e}")
        return False

def batch_sync(links_file=LINKS_FILE):
    """批量同步文章"""
    log("\n" + "="*50)
    log("=== 哲学园全自动批量同步系统 ===")
    log("="*50)
    
    if not os.path.exists(links_file):
        log(f"[错误] 错误：找不到链接文件 {links_file}")
        log(f"请创建 {links_file} 文件，每行一个链接，格式：")
        log("  链接 [分类编号]")
        log("例如：")
        log("  https://mp.weixin.qq.com/s/xxxxx 1")
        log("  https://mp.weixin.qq.com/s/yyyyy 1")
        log("")
        log("分类编号：1=老蝉专栏, 2=古希腊, 3=形而上学, 4=伦理学")
        log("         5=认识论, 6=逻辑学, 7=美学, 8=数理科哲")
        return
    
    # 读取链接
    with open(links_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not lines:
        log("[警告] 链接文件为空")
        return
    
    log(f"[信息] 共找到 {len(lines)} 个待处理链接")
    
    success_count = 0
    fail_count = 0
    
    for i, line in enumerate(lines, 1):
        log(f"\n[{i}/{len(lines)}] 处理中...")
        
        # 解析链接和分类
        parts = line.split()
        url = parts[0]
        category_id = parts[1] if len(parts) > 1 else "1"
        
        # 下载文章
        if download_article(url, category_id):
            success_count += 1
        else:
            fail_count += 1
        
        # 避免请求过快
        if i < len(lines):
            time.sleep(2)
    
    log(f"\n{'='*50}")
    log(f"[统计] 批量处理完成：成功 {success_count} 篇，失败 {fail_count} 篇")
    log(f"{'='*50}\n")
    
    # 自动推送到GitHub
    if success_count > 0:
        log("[推送] 开始推送到GitHub...")
        git_push()
    
    return success_count, fail_count

def interactive_mode():
    """交互式单篇模式（保留原功能）"""
    print("=== 哲学园一键同步 (交互模式) ===")
    
    if not os.path.exists(INDEX_FILE):
        print(f"[错误] 错误：在脚本旁边没找到 {INDEX_FILE}")
        return

    url = input("请输入微信文章链接: ").strip()
    if not url:
        return
    
    print("\n请选择文章分类:")
    for key, value in CAT_NAMES.items():
        num = [k for k, v in CAT_MAP.items() if v == key][0]
        print(f"  [{num}] {value}")
    
    category_id = CAT_MAP.get(input("请输入编号 (默认'1'): ").strip(), "laochan-column")
    
    if download_article(url, category_id):
        git_push()
    
    input("\n按回车退出...")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == "--batch" or sys.argv[1] == "-b":
            # 批量模式
            links_file = sys.argv[2] if len(sys.argv) > 2 else LINKS_FILE
            batch_sync(links_file)
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("哲学园文章同步工具")
            print("")
            print("用法:")
            print("  python sync.py              - 交互式单篇模式")
            print("  python sync.py --batch      - 批量模式（读取links.txt）")
            print("  python sync.py --batch file - 批量模式（读取指定文件）")
            print("")
            print("links.txt 格式:")
            print("  # 这是注释")
            print("  https://mp.weixin.qq.com/s/xxxxx 1")
            print("  https://mp.weixin.qq.com/s/yyyyy 2")
            print("")
            print("分类编号：")
            for num, cat in CAT_MAP.items():
                print(f"  {num} = {CAT_NAMES[cat]}")
        else:
            print(f"未知参数: {sys.argv[1]}")
            print("使用 --help 查看帮助")
    else:
        # 默认交互模式
        interactive_mode()
