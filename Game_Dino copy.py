#Program Name: Game_Dino
#Date: 26/02/2023 

# play game in url: chrome://dino/
# learn more: https://pypi.org/project/PyAutoGUI/  and  https://pyautogui.readthedocs.io/en/latest/
# Check this url: https://www.geeksforgeeks.org/keyboard-module-in-python/

import time

import pyautogui  # pip install pyautogui >> pip install --upgrade pyautogui >> pip show pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray # pip install numpy

def isCollide(data):
    # Draw rectangle for Birds
    for i in range(390, 399): #x-axis
        for j in range(250,380): #y-axis
            if data[i,j] < 100:
                # pyautogui.keyUp('up')
                pyautogui.keyDown('down')  
                time.sleep(0.5)
                pyautogui.keyUp('down')              
                return
    # Draw rectangle for Cactus
    for i in range(410,420): #x-axis
        for j in range(390,460): #y-axis
            if data[i, j] < 100:
                # pyautogui.keyUp('down')                
                pyautogui.keyDown('up')              
                return            
    return

# def takeScreenShot():
#     image = ImageGrab.grab().convert('L')
#     # image.show()
#     return image

if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(pyautogui.size())
        
        isCollide(data)
        
        #     pyautogui.press('up')
        #     print("this is a collide")
        
        # print(asarray(image))
        
        # # Draw rectangle for Birds
        # for i in range(360, 390):
        #     for j in range(250,380):
        #         data[i,j] = 170
        
        # # Draw rectangle for Cactus
        # for i in range(380, 410):
        #     for j in range(390,460):
        #         data[i,j] = 100
        # image.show()
        # break