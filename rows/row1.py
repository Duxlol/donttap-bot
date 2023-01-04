from pyautogui import *
import pyautogui
import time

def row1():
    #first row
    if pyautogui.pixel(700, 313)[0] == 0:
        pyautogui.click(700, 313)
    if pyautogui.pixel(880 , 313)[0] == 0:
        pyautogui.click(880, 313)
    if pyautogui.pixel(1050, 300)[0] == 0:
        pyautogui.click(1050, 313)
    if pyautogui.pixel(1200, 313)[0] == 0:
        pyautogui.click(1200, 313)