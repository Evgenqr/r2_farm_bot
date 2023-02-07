import numpy as np
import pyscreenshot
import time
import pytesseract
import cv2
import mouse
from win32api import keybd_event
import win32con

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def check_mob():
    # берем в таргет
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # f
    time.sleep(.3)
    mouse.press(button='left')
    time.sleep(.3)
    mouse.press(button='right')
    time.sleep(.3)
    mouse.release(button='left')
    mouse.release(button='right')
    # распосзнавание текста в таргете
    x0, y0 = 856, 961  # main home
    xl = x0 + 40
    xr = x0 + 150
    yd = y0 - 33
    yt = y0 - 10
    screen = np.array(pyscreenshot.grab(bbox=(xl, yd, xr, yt)))
    filename = 'image.png'
    cv2.imwrite(filename, screen)
    image = cv2.imread('Image.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # распознаем текст со скриншота
    thresh = cv2.resize(thresh, (800, 250))
    text = pytesseract.image_to_string(thresh, lang='rus', config='--psm 6')
    index = text.find('Мантикора')
    index2 = text.find('кора')
    if index == -1 and index2 == -1:
        # # Снимаем таргет
        mouse.press(button='left')
        time.sleep(.3)
        mouse.release(button='left')
        time.sleep(.3)
        keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
        # ищем дальше
    else:
        # Снимаем таргет
        keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(2)
        keybd_event(0x70, 0, 0, 0)
        time.sleep(2)
        keybd_event(0x70, 0, 0, 0)
        time.sleep(4)
        keybd_event(0x45, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # e
        time.sleep(.8)
        keybd_event(0x45, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.5)
        keybd_event(0x45, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # e
        time.sleep(.8)
        keybd_event(0x45, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.5)
        keybd_event(0x45, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # e
        time.sleep(.8)
        keybd_event(0x45, 0, win32con.KEYEVENTF_KEYUP, 0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    check_mob()
