from ReportBot import *
import schedule
import time
def run():
    reportBot = ReportBot()
    reportBot.run()
def resetCsv():
    reportBot = ReportBot()
    reportBot.resetCsv()


if __name__ == '__main__':
    run()
    schedule.every().day.at("07:00").do(run)
    schedule.every().day.at("11:00").do(run)
    schedule.every().day.at("15:00").do(run)
    schedule.every().day.at("19:00").do(run)
    schedule.every().day.at("23:00").do(run)
    schedule.every().day.at("22:56").do(run)
    # schedule.every().day.at("00:00").do(resetCsv).when(lambda x: x.day == 1)
    while True:
        schedule.run_pending()
        time.sleep(1)