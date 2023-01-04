from pyautogui import *
import pyautogui
import time

def row3():
        #third row
    if pyautogui.pixel(700, 640)[0] == 0:
        pyautogui.click(700, 640)
    if pyautogui.pixel(880 , 640)[0] == 0:
        pyautogui.click(880, 640)
    if pyautogui.pixel(1050, 640)[0] == 0:
        pyautogui.click(1050, 640)
    if pyautogui.pixel(1200, 640)[0] == 0:
        pyautogui.click(1200, 640)