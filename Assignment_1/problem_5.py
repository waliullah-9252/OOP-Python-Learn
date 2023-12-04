import pyautogui
from time import sleep
n = int(input())
sleep(3)
for i in range(1,n+1):
    pyautogui.write('#'*i, interval=0.25)
    pyautogui.press('enter')















