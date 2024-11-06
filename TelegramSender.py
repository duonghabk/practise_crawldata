import requests
from config import *

class TelegramSender():
    def __init__(self) -> None:
       pass

    def sendMessage(self, document):
        document = "hahahahaha"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={str(document)}"
        requests.get(url)