# 哲学园文章全自动同步工具

## 功能说明

这个工具可以从微信公号"哲学园"自动搬运文章到你的网站，并自动推送到GitHub。

## 工作方式

1. 你在 `links.txt` 中添加微信文章链接（每行一个）
2. 运行同步程序，自动下载文章、保存图片、更新首页
3. 自动推送到GitHub仓库

## 使用步骤

### 1. 准备文章链接

编辑 `links.txt` 文件，添加要同步的文章链接：

```
# 格式：链接 [分类编号]
# 分类：1=老蝉专栏, 2=古希腊, 3=形而上学, 4=伦理学, 5=认识论, 6=逻辑学, 7=美学, 8=数理科哲

https://mp.weixin.qq.com/s/xxxxx 1
https://mp.weixin.qq.com/s/yyyyy 1
```

### 2. 运行同步

#### 方式一：立即运行（推荐）
双击 `run_now.bat` 即可立即执行同步

#### 方式二：命令行运行
```bash
# 批量模式
python sync.py --batch

# 单篇交互模式
python sync.py
```

### 3. 设置定时自动运行（可选）

双击 `setup_task.bat`，设置每天自动运行

默认时间：每天凌晨 2:00

### 4. 查看日志

同步记录会保存在 `sync.log` 文件中

## 文件说明

- `sync.py` - 主程序
- `links.txt` - 文章链接列表
- `run_now.bat` - 立即运行脚本
- `setup_task.bat` - 设置定时任务
- `sync.log` - 同步日志
- `articles/` - 文章存放目录
- `index.html` - 网站首页

## 注意事项

1. **GitHub配置**：确保已配置好GitHub登录凭证，可以免密推送
2. **分类选择**：如果不确定分类，默认使用1（老蝉专栏）
3. **网络问题**：如果下载失败，可以多次运行程序，会自动跳过已存在的文章
4. **定时任务**：如需修改时间，请打开Windows"任务计划程序"进行修改

## 命令行参数

```bash
python sync.py --help          # 显示帮助
python sync.py                 # 交互式单篇模式
python sync.py --batch         # 批量模式（读取links.txt）
python sync.py --batch file    # 批量模式（读取指定文件）
```
