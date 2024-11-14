from Fetcher import Fetcher
from TelegramSender import TelegramSender
import pandas as pd


class ReportBot():
    def __init__(self) -> None:
        self.fetcher = Fetcher()
        self.telegramSender = TelegramSender()

    def run(self):
        self.oldData = self.fetcher.readFromFile()        
        self.newData = self.fetcher.request()
        self._updateData()
        self.fetcher.saveToFile(self.oldData)
        self.telegramSender.sendMessage(self.newData)


    def _updateData(self):        
        self.newData = pd.DataFrame(self.newData['Name'])
        if 'number' not in self.oldData.columns:
            # Create the 'X' column with default value 0
            self.oldData['number'] = 0        

        # Merge the DataFrames on the 'value' column
        merged_df = self.newData.merge(self.oldData, on='Name', how='outer')

        # Increment the 'number' column where the merge was successful
        merged_df['number'] = merged_df['number'].fillna(0).astype(int) + 1

        # Update df_A and create 'number' column in df_B
        self.oldData = merged_df[['Name', 'number']].drop_duplicates()
        self.newData['number'] = merged_df['number']

    def resetCsv(self):
        self.fetcher.saveToFile(pd.DataFrame({}))

