import sys
import time
import pyautogui
from PIL import Image
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from python_imagesearch.imagesearch import imagesearch

keyboard = KeyboardController()
mouse = MouseController()

def recognize():
    img = pyautogui.screenshot('screen.png', region=(629, 232, 646, 646))
    pos = imagesearch('black.png', 629, 232, 646, 646)
    if pos[0] != -1:
        print("Black square found at:", pos[0], pos[1])
        time.sleep(1)
        pyautogui.click(pos[0], pos[1])
        sys.exit