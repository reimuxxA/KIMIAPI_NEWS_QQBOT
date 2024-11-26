# KIMIAPI_NEWS_QQBOT
One solution for QQ group news(Mainly for personal use(主要自用))

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
```
   git clone https://github.com/yourusername/news_summarizeQbot.git
   cd news_summarizeQbot
```
2. **创建虚拟环境（可选）**
```
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. **安装依赖**
```
pip install -r requirements.txt
```
4. **配置环境**
 在config.py填写相关数据

5. **NapCatqq**
此事在官方文档亦有记载（观看文档）
登录之后，在NapCat/config/onebot11_XXXX.json 修改

```
{
  "network": {
    "httpServers": [
      {
        "name": "httpServer",
        "enable": true,
        "port": 3000,
        "host": "0.0.0.0",
        "enableCors": true,
        "enableWebsocket": true,
        "messagePostFormat": "array",
        "token": "和config.py的保持一致",
        "debug": false
      }
    ],
    "httpClients": [],
    "websocketServers": [
      {
        "name": "WsServer",
        "enable": true,
        "host": "0.0.0.0",
        "port": 3001,
        "messagePostFormat": "array",
        "reportSelfMessage": false,
        "token": "和config.py的保持一致",
        "enableForcePushEvent": true,
        "debug": false,
        "heartInterval": 30000
      }
    ],
    "websocketClients": []
  },
  "musicSignUrl": "",
  "enableLocalFile2Url": false,
  "parseMultMsg": true
}
```

启动NapCat

[NapCatQQ](https://napcat.napneko.icu/guide/start-install)

5. **最后步骤**
```
python main.py
```
