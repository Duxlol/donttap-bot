import pyautogui
import time

def row4():
        #fourth row
    if pyautogui.pixel(700, 800)[0] == 0:
        pyautogui.click(700, 800)
    if pyautogui.pixel(880 , 800)[0] == 0:
        pyautogui.click(880, 800)
    if pyautogui.pixel(1050, 800)[0] == 0:
        pyautogui.click(1050, 800)
    if pyautogui.pixel(1200, 800)[0] == 0:
        pyautogui.click(1200, 800)