from Fetcher import Fetcher
from TelegramSender import TelegramSender



class ReportBot():
    def __init__(self) -> None:
        self.fetcher = Fetcher()
        self.telegramSender = TelegramSender()

    def run(self):
        # self.oldData = self.fetcher.readFromFile()
        # dataReponse = self.newData = self.fetcher.request()
        # self.fetcher.saveToFile(dataReponse)
        # self._updateData(self.newData,self.oldData)
        # self.fetcher.saveToFile()
        self.telegramSender.sendMessage("dataReponse")


    def _updateData(self, newData, oldData):
        pass
