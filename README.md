# 你的日记（NiDiary）导出工具

这是一个用于从 [你的日记（nideriji.cn）](https://nideriji.cn) 导出个人日记内容并生成 Word 文档的 Python 脚本。支持自动下载内嵌图片，并按时间顺序整理成 `.docx` 文件。

---

## 📦 功能特性

- ✅ 自动登录你的日记账号
- ✅ 获取所有日记条目
- ✅ 下载日记中嵌入的图片（格式如 `[图1]`）
- ✅ 按时间顺序生成带标题的 Word 文档
- ✅ 支持中文字体（默认使用「微软雅黑」）

---

## 🛠️ 依赖库

本脚本依赖以下 Python 第三方库：

- `requests`：用于 HTTP 请求
- `python-docx`：用于生成 Word 文档
- `re`、`time`、`os`、`json`：标准库，无需额外安装

安装依赖：

```bash
pip install requests python-docx
```

> 注意：`python-docx` 的包名为 `python-docx`，但导入时使用 `from docx import Document`。

---

## 🔐 使用方法

1. **填写账号信息**

   打开 `main()` 函数，填入你的你的日记账号邮箱和密码：

   ```python
   logins = login('your_email@example.com', 'your_password')
   ```

2. **运行脚本**

   ```bash
   python nideriji_exporter.py
   ```

3. **输出结果**

   脚本执行完成后，会在当前目录生成：
   - 多个图片文件（如 `1.jpg`, `2.jpg`...）
   - 一个名为 `nideriji_diaries.docx` 的 Word 文档，包含所有日记内容和图片

---

## 📁 文件结构说明

- `nideriji_exporter.py`：主脚本
- `*.jpg`：下载的日记配图（临时文件，可手动清理）
- `nideriji_diaries.docx`：最终导出的 Word 文档

---

## ⚠️ 注意事项

- 本工具仅用于**个人数据备份**，请勿用于批量爬取或商业用途。
- 你的日记网站可能更新 API 或增加验证机制（如验证码、CSRF 令牌），若脚本失效请自行调试或提交 Issue。
- 脚本默认使用空的 `csrfmiddlewaretoken`，如遇登录失败，可尝试先访问登录页获取真实 token。
- 图片下载依赖于 `https://f.nideriji.cn` 域名，请确保网络可访问。

---

## 📜 许可证

本项目为个人用途脚本，无明确开源许可证。欢迎学习、修改和分享，但请遵守你的日记网站的[服务条款](https://nideriji.cn)。

---

## 🙏 致谢

感谢 [你的日记](https://nideriji.cn) 提供简洁温暖的记录平台 ❤️

---

> ✨ **提示**：如果你希望导出为 PDF、Markdown 或其他格式，可基于此脚本扩展功能。欢迎提交 PR！
