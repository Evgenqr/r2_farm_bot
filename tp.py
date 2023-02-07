import pyautogui
from time import sleep
from win32api import keybd_event
import win32con


def start_tp(t=1):
    # 0 = home
    keybd_event(0x0D, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    sleep(0.3)
    keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
    sleep(0.3)
    keybd_event(0x0D, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    sleep(0.3)
    keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
    tp = pyautogui.locateOnScreen('img-tp/' + str(t) + '.png',
                                  confidence=0.9)
    if tp is None:
        keybd_event(0x0D, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        sleep(0.3)
        keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.3)
        keybd_event(0x0D, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        sleep(0.3)
        keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
        x, y = pyautogui.locateCenterOnScreen('img-tp/' + str(t) + '.png',
                                              confidence=0.9)
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
        # sleep(2)
        return t
    else:
        x, y = pyautogui.locateCenterOnScreen('img-tp/' + str(t) + '.png',
                                              confidence=0.9)
        pyautogui.moveTo(x, y)
        pyautogui.doubleClick()
        # sleep(2)
        return t
