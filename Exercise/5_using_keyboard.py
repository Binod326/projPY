# Check this url: https://www.geeksforgeeks.org/keyboard-module-in-python/

import keyboard                 #pip install keyboard

def on_key_press(event):
    print('Key pressed:', event.name)
    if event.name == 'b':
        print('You pressed the "b" key!', "Event type:", event.event_type)
    elif event.name == 'e':
        print('Terminating program...')
        keyboard.unhook_all()   # Unhook all keyboard events
        exit()                  # Exit the program

keyboard.on_press(on_key_press)

# Keep the program running until a key 'e' is pressed
keyboard.wait('e')              



# import keyboard                 #pip install keyboard
# import time
# def on_key_press(event):
#     print('Key pressed:', event.name)
#     if event.name == 'b':
#         print('You pressed the "b" key!', "Event type:", event.event_type)
#     elif event.name == 'e':
#         print('Terminating program... \nPress Ctrl+C to exit the program.')
#         keyboard.unhook_all()   # Unhook all keyboard events
#         raise SystemExit         # Raise an exception to exit the program

# keyboard.on_press(on_key_press)

# # Main loop
# while True:
#     try:
#         time.sleep(0.1)  # Sleep briefly to avoid CPU usage
#     except KeyboardInterrupt:
#         break  # Terminate the loop if Ctrl+C is pressed



# import keyboard
# import time

# def on_key_press(event):
#     if event.name == 'b' and event.event_type == 'down':
#         print(f'You pressed the "b" key at time {time.time()}')
#     elif event.name == 'e' and event.event_type == 'down':
#         print('Terminating program...')
#         keyboard.unhook_all()  # Unhook all keyboard events
#         exit()  # Exit the program

# keyboard.on_press(on_key_press)

# # Keep the program running until a key is pressed
# keyboard.wait()           # To stop this program, select the terminal window and then press Ctrl+C  