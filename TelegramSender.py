import requests
from config import *
from datetime import datetime

class TelegramSender():
    def __init__(self) -> None:
       pass

    def sendMessage(self, document):
        content = str(datetime.now()) + document.to_string(index=False, header=False)
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={content}"
        requests.get(url)