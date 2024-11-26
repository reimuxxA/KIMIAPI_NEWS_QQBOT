# utils/kimi_api.py
from typing import Dict, Any
import os
import json
from openai import OpenAI, RateLimitError  # 导入 RateLimitError
from openai.types.chat.chat_completion import Choice
from config import KIMI_API_KEY
from utils.logger import logger
import time

# 初始化 OpenAI 客户端
client = OpenAI(
    base_url="https://api.moonshot.cn/v1",
    api_key=KIMI_API_KEY,
)

# 定义 search_impl 函数
def search_impl(arguments: Dict[str, Any]) -> Any:
    """
    对于内置的 $web_search 函数，我们只需要原封不动地返回 arguments 即可。
    """
    return arguments

# 定义 chat 函数
def chat(messages) -> Choice:
    max_retries = 3
    retry_delay = 2  # 重试间隔时间（秒）
    for attempt in range(max_retries + 1):
        try:
            completion = client.chat.completions.create(
                model="moonshot-v1-128k",
                messages=messages,
                temperature=0.3,
                tools=[
                    {
                        "type": "builtin_function",  # 使用 builtin_function 声明 $web_search 函数
                        "function": {
                            "name": "$web_search",
                        },
                    }
                ]
            )
            return completion.choices[0]
        except RateLimitError as e:  # 处理 RateLimitError
            if attempt < max_retries:
                logger.warning(f"Rate limit exceeded. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
            else:
                logger.error(f"Max retries reached. Unable to complete request due to rate limit.")
                raise
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

# 定义 fetch_news 函数
def fetch_news(query, start_date, end_date):
    messages = [
        {"role": "system", "content": "你是 Kimi。"},
        {"role": "user", "content": f"请搜索 {query}，时间范围从 {start_date} 到 {end_date}。"}
    ]

    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        choice = chat(messages)
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls":  # 判断当前返回内容是否包含 tool_calls
            messages.append(choice.message)  # 将 Kimi 大模型返回的 assistant 消息添加到上下文中
            for tool_call in choice.message.tool_calls:  # tool_calls 可能是多个，因此我们使用循环逐个执行
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(tool_call.function.arguments)  # 反序列化 arguments
                if tool_call_name == "$web_search":
                    tool_result = search_impl(tool_call_arguments)
                else:
                    tool_result = f"Error: unable to find tool by name '{tool_call_name}'"

                # 构造 role=tool 的 message，提交工具调用结果
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result),  # 序列化工具调用结果
                })

    logger.info("Fetched news successfully")
    return choice.message.content  # 返回模型生成的最终回复

# 定义 format_news 函数
def format_news(news_items):
    formatted_news = "每周新闻（基于KIMI api）\n"
    for item in news_items:
        formatted_news += f"- {item['title']} ({item['url']})\n"
    return formatted_news