import pyautogui
import time
import random
import os
curentPath = str(os.path.dirname(os.path.abspath(__file__)))
def auto_click(x,y):

    while(True):
        current_position = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(current_position.x, current_position.y)
        time.sleep(180)

def get_position_mouse():
    time.sleep(2)
    x, y = pyautogui.position()
    print(x,y)

def autoAnswer():
    while(True):
        try:            
            randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_' + str(random.randint(1, 4)) + '.png')            
        except:
            if pyautogui.locateCenterOnScreen(curentPath + '/Ans_1.png'):
                randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_1.png')
            elif pyautogui.locateCenterOnScreen(curentPath + '/Ans_2.png'):
                randomAnswer = pyautogui.locateCenterOnScreen(curentPath + '/Ans_2.png')
        pyautogui.click(randomAnswer.x, randomAnswer.y)
        time.sleep(5)

        try:   
            pyautogui.scroll(-10000)      
            time.sleep(1)   
            nextButton = pyautogui.locateCenterOnScreen(curentPath + '/NextButton_2.png')
            pyautogui.click(nextButton.x, nextButton.y)
        except:
            finishButton = pyautogui.locateCenterOnScreen(curentPath + '/Finished.png')
            pyautogui.click(finishButton.x, finishButton.y)
            break
        

# get_position_mouse()
# auto_click(387,326)
# auto_click(272, 312)
autoAnswer()