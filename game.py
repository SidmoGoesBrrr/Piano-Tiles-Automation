from pyautogui import *
import time
import keyboard
import win32api, win32con
import pyautogui

#pyautogui.displayMousePosition() #Use this to get the position of the tiles

#Tile 1 (597, 555) RGB: (255, 255, 255)
#Tile 2 (690, 555) RGB: (255, 255, 255)
#Tile 3 (778, 555) RGB: (255, 255, 255)
#Tile 4 (846, 555) RGB: (255, 255, 255)

def click(x,y):
    print("Clicking")
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #Using win32api instead of pyautogui to click because pyautogui is slow
    time.sleep(0.15)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Clicked")


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(597, 555)[0] == 0:
        click(597, 555)
    if pyautogui.pixel(690, 555)[0] == 0:
        click(690, 555)
    if pyautogui.pixel(778, 555)[0] == 0:
        click(778, 555)
    if pyautogui.pixel(846, 555)[0] == 0:
        click(846, 555)