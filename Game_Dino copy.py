#Program Name: Game_Dino
#Date: 26/02/2023 

# play game in url: chrome://dino/
# learn more: https://pypi.org/project/PyAutoGUI/  and  https://pyautogui.readthedocs.io/en/latest/
# Check this url: https://www.geeksforgeeks.org/keyboard-module-in-python/

import pyautogui # pip install pyautogui >> pip install --upgrade pyautogui >> pip show pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time
# from numpy import asarray # pip install numpy

def isCollide(data):
        # Draw rectangle for Cactus
        for i in range(1800,1810):
            for j in range(1230,1250):
                if data[i, j] < 100:
                     pyautogui.keyDown('up')
                    #  print(data[i, j])
                     return
                
        # Draw rectangle for Birds
        # for i in range(800, 850):
        #     for j in range(700,1100):
        #         if data[i,j] < 100:
        #             pyautogui.keyDown('down')
        #             return
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
        # for i in range(1800, 1850):
        #     for j in range(700,1100):
        #         data[i,j] = 170
        
        # # Draw rectangle for Cactus
        # for i in range(800, 850):
        #         data[i,j] = 100
        # image.show()
        # break

#pygui test
# pyautogui.keyDown('b')
# pyautogui.keyDown('i')
# pyautogui.keyDown('n')
# pyautogui.keyDown('o')
# pyautogui.keyDown('d')
# pyautogui.keyDown(' ')  


# # Main loop
# while True:
#     try:
#         time.sleep(0.1)  # Sleep briefly to avoid CPU usage
#     except KeyboardInterrupt:
#         break  # Terminate the loop if Ctrl+C is pressed
