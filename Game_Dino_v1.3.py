#Program Name: Game_Dino
#Date: 03/03/2023 

# play game in url: chrome://dino/
# learn more: https://pypi.org/project/PyAutoGUI/  and  https://pyautogui.readthedocs.io/en/latest/
# Check this url: https://www.geeksforgeeks.org/keyboard-module-in-python/

import time
# import datetime as date
import pyautogui  # pip install pyautogui >> pip install --upgrade pyautogui >> pip show pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray # pip install numpy
x_axis_range = range(365, 400)
y_axis_range_bird = range(250, 340)
y_axis_range_cactus = range(341, 440)

def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.18)
    pyautogui.keyUp("down")
    return

def playDayMode(data):
    # Draw rectangle for Birds
    for i in x_axis_range: #x-axis
        for j in y_axis_range_bird: #y-axis
            if data[i,j] < 100:
                hit('down')
                return
    # Draw rectangle for Cactus
    for i in x_axis_range: #x-axis 405
        for j in y_axis_range_cactus: #y-axis
            if data[i, j] < 100:                
                hit('up')            
                return            
    return

def playNightMode(data):
    # Draw rectangle for Birds
    for i in x_axis_range: #x-axis
        for j in y_axis_range_bird: #y-axis
            if data[i,j] > 150:
                hit('down')
                return
    # Draw rectangle for Cactus
    for i in x_axis_range: #x-axis
        for j in y_axis_range_cactus: #y-axis
            if data[i, j] > 150:                
                hit('up')             
                return            
    return

if __name__ == "__main__":
    print('Hey.. dino game is about to begin in 3 seconds')
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(pyautogui.size())
        
        # Check if it is dark night
        counter = 0
        for i in range(1,400):
            if data[i,600]<127: # try with the value 255/2 = 127 instead of 100
                counter=+i      # count how many pixel the light is below 100
            # # draw line where we tried to detect mode
            # data[i,600] = 100
        # print(counter)

        if counter < 100:
            # print('day mode')
            playDayMode(data)
        else:
            # print('night mode', date.datetime.today())
            playNightMode(data)

        # image.show()
        # break
        
        # print(asarray(image))
        
        # # Draw rectangle for Birds
        # for i in x_axis_range: #x-axis
        #     for j in y_axis_range_bird: #y-axis
        #         data[i,j] = 170
        # # Draw rectangle for Cactus
        # for i in x_axis_range: #x-axis
        #     for j in y_axis_range_cactus: #y-axis
        #         data[i,j] = 100
        # image.show()
        # break