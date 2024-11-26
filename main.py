# main.py
import schedule
import time
from datetime import datetime, timedelta
from utils.kimi_api import fetch_news, format_news
from utils.qq_bot import send_message_to_group
from utils.logger import logger
import random

def get_last_week_dates():
    today = datetime.now()
    one_week_ago = today - timedelta(days=7)
    start_date = one_week_ago.strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    return start_date, end_date

def fetch_and_send_news():
    start_date, end_date = get_last_week_dates()
    
    # 获取 AI 行业相关新闻
    ai_news_query = 'AI 行业 新闻'
    ai_news_items = fetch_news(ai_news_query, start_date, end_date)
    time.sleep(random.uniform(10, 30))  # 随机暂停 1 到 3 秒
    
    # 获取 AI 开源项目更新
    ai_project_query = 'AI 开源项目'
    ai_project_items = fetch_news(ai_project_query, start_date, end_date)
    time.sleep(random.uniform(10, 30))  # 随机暂停 1 到 3 秒
    
    # 获取电脑硬件快讯
    hardware_query = '电脑硬件 快讯'
    hardware_items = fetch_news(hardware_query, start_date, end_date)
    time.sleep(random.uniform(10, 30))  # 随机暂停 1 到 3 秒
    
    # 合并所有消息
    full_message = f"{ai_news_items}\n\n{ai_project_items}\n\n{hardware_items}"
    
    # 发送消息到 QQ 群聊
    send_message_to_group(full_message)
    logger.info("News and updates sent successfully")

def main():
    # 每周五早晨8点执行任务
    schedule.every().friday.at("08:00").do(fetch_and_send_news)
    
    # 手动触发任务
    fetch_and_send_news()
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()