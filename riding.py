import pyautogui
import time

'''
This is a simple script to level your riding
This script will press and hold the 'S' and 'A' keys
Make sure you and your horse are fully fed
You can run this overnight without any issues, it will run you backwards in a circle until you stop it
'''

time.sleep(4)
try:
    print("Pressing and holding 'S' and 'A' keys. Press CTRL+C to stop.")
    pyautogui.keyDown('s')  # Press the S key down.
    pyautogui.keyDown('a')  # Press the A key down.
    
    # This loop is here to keep the script running.
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nReleasing 'S' and 'A' keys.")
    pyautogui.keyUp('s')  # Release the S key.
    pyautogui.keyUp('a')  # Release the A key.
