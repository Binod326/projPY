#Author: Binod Maharjan
#Program Name: Game_Dino
#Date: 26/02/2023 
#Version: 1.0.0
#Version date: 26/02/2023

# play game in url: chrome://dino/
# 

import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def takeScreenShot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    time.sleep(2)
    takeScreenShot()   

#pygui test
# pyautogui.keyDown('b')
# pyautogui.keyDown('i')
# pyautogui.keyDown('n')
# pyautogui.keyDown('o')
# pyautogui.keyDown('d')
# pyautogui.keyDown(' ')  