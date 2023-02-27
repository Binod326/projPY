#Author: Binod Maharjan
#Program Name: Game_Dino
#Date: 26/02/2023 
#Version: 1.0.0
#Version date: 26/02/2023

# play game in url: chrome://dino/
# learn more: https://pypi.org/project/PyAutoGUI/  and  https://pyautogui.readthedocs.io/en/latest/

# import pyautogui # pip install pyautogui >> pip install --upgrade pyautogui >> pip show pyautogui
# from PIL import Image, ImageGrab # pip install pillow
# import time

# def takeScreenShot():
#     image = ImageGrab.grab()
#     image.show()

# if __name__ == "__main__":
#     time.sleep(2)
#     takeScreenShot()   





#pygui test
# pyautogui.keyDown('b')
# pyautogui.keyDown('i')
# pyautogui.keyDown('n')
# pyautogui.keyDown('o')
# pyautogui.keyDown('d')
# pyautogui.keyDown(' ')  


# Here's an example modification to the code that starts a function with a print statement when the "up" key is pressed:
import pyautogui
import time

def on_key_press(key):
    if key == 'b':
        print(f'You pressed the "b" key at time {time.time()}')
    elif key == 'e':
        print('Terminating program...')
        raise SystemExit
    elif key == 'up':
        print('Starting function...')
        my_function()

def my_function():
    print('This is my function!')

# Start listening for key presses
pyautogui.onKey(on_key_press)

# Main loop
while True:
    try:
        time.sleep(0.1)  # Sleep briefly to avoid CPU usage
    except KeyboardInterrupt:
        break  # Terminate the loop if Ctrl+C is pressed
