import pyautogui
import time
import random
import os
curentPath = str(os.path.dirname(os.path.abspath(__file__)))
def auto_click(x,y):
        current_position = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(current_position.x, current_position.y)
        time.sleep(1)

def get_position_mouse():
    time.sleep(2)
    x, y = pyautogui.position()
    print(x,y)

def autoAnswer():
        try:
            randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_' + str(random.randint(1, 4)) + '_.png')
        except:
            if pyautogui.locateCenterOnScreen(curentPath + '/Ans_1_.png'):
                randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_1_.png')
            elif pyautogui.locateCenterOnScreen(curentPath + '/Ans_2_.png'):
                randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_2_.png')
        pyautogui.click(randomAnswer.x, randomAnswer.y)
        time.sleep(5)

        try:
            pyautogui.scroll(-10000)
            time.sleep(2)
            nextButton = pyautogui.locateCenterOnScreen(curentPath + '/NextButton_.png')
            pyautogui.click(nextButton.x, nextButton.y)
        except:
            finishButton = pyautogui.locateCenterOnScreen(curentPath + '/Finished_.png')
            pyautogui.click(finishButton.x, finishButton.y)

time.sleep(10)
while(1):
    # get_position_mouse()
    # auto_click(387,326)
    # auto_click(272, 312)

    #click icon name team
    # name = pyautogui.locateCenterOnScreen(curentPath + '/name.png')
    # pyautogui.click(name.x, name.y)
    #click name icon team
    auto_click(1319, 122)
    autoAnswer()