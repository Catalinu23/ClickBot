import pywinauto
import time
import win32api

while(1):
    x, y = win32api.GetCursorPos()
    pywinauto.mouse.click(button='left',coords=(x,y))
    time.sleep(0.1)

k = input()
