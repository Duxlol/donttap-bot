import cv2
import pyautogui

method = cv2.TM_SQDIFF_NORMED

img = pyautogui.screenshot('screen.png', region=(629, 232, 646, 646))

small_image = cv2.imread('blackk.png')
large_image = cv2.imread('screen.png')

result = cv2.matchTemplate(small_image, large_image, method)

mn,_,mnLoc,_ = cv2.minMaxLoc(result)

MPx,MPy = mnLoc

trows,tcols = small_image.shape[:2]

cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
cv2.imshow('output',large_image)
cv2.waitKey(0)