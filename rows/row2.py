from pyautogui import *
import pyautogui
import time

def row2():
        #second row
    if pyautogui.pixel(700, 470)[0] == 0:
        pyautogui.click(700, 470)
    if pyautogui.pixel(880 , 470)[0] == 0:
        pyautogui.click(880, 470)
    if pyautogui.pixel(1050, 470)[0] == 0:
        pyautogui.click(1050, 470)
    if pyautogui.pixel(1200, 470)[0] == 0:
        pyautogui.click(1200, 470)