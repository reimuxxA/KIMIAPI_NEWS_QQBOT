# utils/qq_bot.py
import requests
from config import QQ_BOT_TOKEN, QQ_GROUP_ID
from utils.logger import logger

def send_message_to_group(message):
    url = f'http://127.0.0.1:3000/send_group_msg'  # 使用 NapCat 的 HTTP 服务端端口
    headers = {
        'Authorization': f'Bearer {QQ_BOT_TOKEN}'
    }
    data = {
        'group_id': QQ_GROUP_ID,
        'message': message
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logger.info("Message sent successfully")
    except requests.RequestException as e:
        logger.error(f"Error sending message: {e}")