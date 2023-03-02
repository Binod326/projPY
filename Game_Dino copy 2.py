#Program Name: Game_Dino
#Date: 26/02/2023 

# play game in url: chrome://dino/
# learn more: https://pypi.org/project/PyAutoGUI/  and  https://pyautogui.readthedocs.io/en/latest/
# Check this url: https://www.geeksforgeeks.org/keyboard-module-in-python/

import time

import pyautogui  # pip install pyautogui >> pip install --upgrade pyautogui >> pip show pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray # pip install numpy

def playDayMode(data):
    # Draw rectangle for Birds
    for i in range(360, 390):
        for j in range(250,380):
            if data[i,j] < 100:
                pyautogui.keyDown('down')
                return

    # Draw rectangle for Cactus
    for i in range(380,410):
        for j in range(390,460):
            if data[i, j] < 100:
                    pyautogui.keyDown('up')
                #  print(data[i, j])
                    return
            
    return

def playNightMode(data):
    # Draw rectangle for Birds
    for i in range(360, 390):
        for j in range(250,380):
            if data[i,j] > 100:
                pyautogui.keyDown('down')
                return

    # Draw rectangle for Cactus
    for i in range(380,410):
        for j in range(390,460):
            if data[i, j] > 100:
                    pyautogui.keyDown('up')
                #  print(data[i, j])
                    return
            
    return

def isCollide(data):
    # Check if it is dark night
    for i in range(1,380):
        if data[i,400]<100:
            print("night mode")
            playNightMode(data)
            return
        else:
            playDayMode(data)

    # # Draw rectangle for Birds
    # for i in range(360, 390):
    #     for j in range(250,380):
    #         if data[i,j] < 100:
    #             pyautogui.keyDown('down')
    #             return

    # # Draw rectangle for Cactus
    # for i in range(380,410):
    #     for j in range(390,460):
    #         if data[i, j] < 100:
    #                 pyautogui.keyDown('up')
    #             #  print(data[i, j])
    #                 return
            
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