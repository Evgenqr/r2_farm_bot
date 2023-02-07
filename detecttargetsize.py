import argparse
import pyautogui
import numpy as np
import pyscreenshot
import time
import pytesseract
import cv2
import sys
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(1.5)
hi = "target.jpg"


def detect_target():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--window", required=True,
                    help="Path to the window image")
    ap.add_argument("-w", "--hi", required=True,
                    help="Path to the hi image")
    args = vars(ap.parse_args())
    window = np.array(pyscreenshot.grab())
    hi = cv2.imread(args["hi"])
    (hiHeight, hiWidth) = hi.shape[:2]
    result = cv2.matchTemplate(window, hi, cv2.TM_CCOEFF)
    (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
    # получаем область вокруг объекта
    topLeft = maxLoc  # верхний левый угол
    # правый нижний угол:
    botRight = (topLeft[0] + hiWidth, topLeft[1] + hiHeight)
    topXY = topLeft
    botXY = botRight
    roi = window[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
    mask = np.zeros(window.shape, dtype="uint8")
    window = cv2.addWeighted(window, 0.55, mask, 0.70, 0)
    window[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
    pyautogui.moveTo(topXY[0], botXY[1])
    x0 = topXY[0]
    y0 = botXY[1]
    return x0, y0


sys.argv = [sys.argv[0], "--window", "window.png", "--hi", hi]
print(detect_target())
