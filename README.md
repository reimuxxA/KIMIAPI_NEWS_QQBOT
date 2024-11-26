# KIMIAPI_NEWS_QQBOT
One solution for QQ group news(Mainly for personal use(主要作用))

## 项目简介

KIMIAPI_NEWS_QQBOT 是一个基于 Kimi API 的新闻汇总机器人。它可以定期从互联网上抓取特定主题的新闻，并将汇总结果发送到指定的 QQ 群聊中。该项目使用 Python 编写，依赖于 OpenAI 的 Kimi API 和 NapCat 的 HTTP 服务。

## 目录结构
news_summarizeQbot/
├── kimi_news_bot/
│   ├── main.py
│   ├── utils/
│   │   ├── kimi_api.py
│   │   ├── qq_bot.py
│   │   └── logger.py
│   └── config.py
└── README.md

## 环境要求

- Python 3.8+
- pip

## 安装步骤

1. **克隆项目**

   git clone https://github.com/yourusername/news_summarizeQbot.git
   cd news_summarizeQbot

2. **创建虚拟环境（可选）**
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. **安装依赖**
pip install -r requirements.txt
