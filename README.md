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


## 项目结构
main.py: 项目的主入口文件，负责调度任务和调用其他模块。
utils/: 包含项目的各种工具模块。
kimi_api.py: 封装了与 Kimi API 交互的函数。
qq_bot.py: 封装了与 QQ 机器人交互的函数。
logger.py: 日志记录模块。
config.py: 项目配置文件，包含 API 密钥和其他配置项。
.env.example: 示例环境变量文件。

## 常见问题
1. **遇到 RateLimitError(大概率不用看，我调的请求频率很长)**
如果你遇到 RateLimitError，这表明你的请求频率超过了 Kimi API 的限制。你可以通过以下方式解决：

降低请求频率：在每次请求之间增加随机暂停时间。
增加重试机制：在 kimi_api.py 中添加对 RateLimitError 的处理，自动重试请求。

如果你需要自定义，去main.py 修改随机范围就可以。
2. **日志文件在哪里？**
日志文件位于项目根目录下的 news_bot.log。你可以通过查看日志文件来获取更多关于运行状态的信息。

3. 如何调整任务时间？
编辑 main.py 中的 schedule 配置：

python
深色版本
schedule.every().friday.at("08:00").do(fetch_and_send_news)
4. 如何调试？
你可以使用 VSCode 或其他 IDE 的调试功能来调试项目。确保在 .vscode/launch.json 中配置好调试设置。

贡献指南
欢迎贡献代码和提出改进建议！请遵循以下步骤：

Fork 本项目。
创建一个新的分支：git checkout -b feature/new-feature。
提交你的更改：git commit -am 'Add new feature'。
推送到你的分支：git push origin feature/new-feature。
提交 Pull Request。
许可证
本项目采用 MIT 许可证，详情请参见 LICENSE 文件。

联系方式
如果有任何问题或建议，请联系 [your-email@example.com]。

感谢你使用 News Summarize Bot！希望它能帮助你更高效地获取和分享新闻信息。
