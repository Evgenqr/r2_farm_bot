import numpy as np
import pyscreenshot as ImageGrab
import time
import pytesseract
import cv2
import sys
# from main import start


hi = "HP.jpg"


def checkHP():
    time.sleep(1)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    x0, y0 = 670, 720
    xl = x0 - 25
    xr = x0 + 11
    yd = y0-2
    yt = y0 + 15
    filename = 'image_hp.png'
    # получаем скрин области экрана
    screen = np.array(ImageGrab.grab(bbox=(xl, yd, xr, yt))) 
    cv2.imwrite(filename, screen)
    image_hp = cv2.imread('Image_hp.png')
    gray = cv2.cvtColor(image_hp, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(
        thresh, lang='rus',
        config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    hp = data[0:5]
    return hp


sys.argv = [sys.argv[0], "--window", "window.png", "--hi", hi]
