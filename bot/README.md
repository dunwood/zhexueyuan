# 哲学园公号文章自动发布 Bot

## 功能说明

本 Skill 自动监控哲学园微信公号新文章，通过 QQ 私信通知你选择发布，自动触发 GitHub Actions 完成搬运。

## 如何找公号 biz 参数

用浏览器打开哲学园公号任意一篇文章，查看地址栏 URL，找到 `__biz=` 后面的值（如 `MzI1NTY3NjA1Mg==`），填入 config.json 的 rsshub_url，完整格式：

```
https://rsshub.app/wechat/mp/MzI1NTY3NjA1Mg==
```

## 填写 config.json

- `rsshub_url`：上一步获取的地址
- `my_qq`：你自己的 QQ 号（收通知的号，不是 Bot 1903241214）

## 确认 gh CLI 已登录

```bash
gh auth status
```

## 在 OpenClaw 服务器上安装此 Skill

```bash
openclaw plugins install ./bot
```

## 安全提醒

config.json 含个人 QQ 号等信息，已加入 .gitignore，不会提交到公开仓库。
