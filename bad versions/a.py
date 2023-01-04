import pyautogui
import time

img = pyautogui.screenshot('screen.png', region=(630,232,644,644))
x, y = pyautogui.locateCenterOnScreen("blackk.png",region=(630,232,644,644))
pyautogui.moveTo(x, y, duration = 0.1)
pyautogui.leftClick()