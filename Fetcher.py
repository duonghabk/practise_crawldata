



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from bs4 import BeautifulSoup

from config import *

binance_future_url = "https://www.binance.com/en/futures/markets/overview-um"
market_future_file = os.getcwd() + "/market_future.csv"
class Fetcher():
    def __init__(self):
        pass


    def _clickButton(self, id):
        self.driver.find_element(by="id", value=id).click()

    def request(self):
        self.driver =  self.setupDriver()
        self.driver.get(binance_future_url)
        time.sleep(2)
        volume24h = self.driver.find_element(by="xpath", value="//*[text()='24h Volume(USD)']")
        volume24h.click()
        volume24h.click()

        header = self.driver.find_element(By.CLASS_NAME, value="bn-table-thead")
        headers = header.find_elements(By.TAG_NAME, 'th')
        # Extract text from headers
        header_titles = [header.text for header in headers]
        row_datas = []
        for i in range(1,4):
            self._clickButton("page-" + str(i))
            row_datas.extend(self._readTable())
        df_result = pd.DataFrame(row_datas, columns=header_titles)

        return df_result

    def _readTable(self):
        row_datas = []
        table = self.driver.find_element(By.CLASS_NAME, value="bn-table-tbody")
        rows = table.find_elements(By.TAG_NAME, 'tr')
        # Iterate over each row
        for index in range(1, len(rows)-1):
            # Find all the cells in the row
            cells = rows[index].find_elements(By.TAG_NAME, 'td')

            # Extract text from each cell
            row_data = [cell.text for cell in cells]
            row_data[0] = row_data[0].replace("\nPerpetual", "")
            if 'USDT' in row_data[0]:               
                row_datas.append(row_data)
        return row_datas


    def setupDriver(self):
        # Set options to make browsing easier
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)


        return driver

    def readFromFile(self):
        try:
            dataframe = pd.read_csv(market_future_file)
        except:
            dataframe = pd.DataFrame({"Name":["USDT"],"number":[0] })
        return dataframe

    def saveToFile(self, dataframe: pd.DataFrame):
        dataframe.to_csv(market_future_file, index=True)

