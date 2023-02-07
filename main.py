import cv2 as cv
from tp import start_tp
import os
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from checkmob import check_mob

# Change the working directory to the folder this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# initialize the WindowCapture class
wincap = WindowCapture('R2')
sleep(3)
# load the trained model
cascade = cv.CascadeClassifier('cascade26.xml')
# load an empty Vision class
vision = Vision()
loop_time = time()


def start():
    k = 1
    while True:
        start_tp(k)
        k += 1
        # get an updated image of the game
        sleep(1)
        screenshot = wincap.get_screenshot()
        # do object detection
        rectangles = cascade.detectMultiScale(screenshot)
        # draw the detection results onto the original image
        cv.imshow('Matches', screenshot)
        rec = len(rectangles)
        if rec > 0:
            r = 0
            while r < rec:
                x = rectangles[r][0]
                y = rectangles[r][1]
                h = rectangles[r][2]
                w = rectangles[r][3]
                point = [x + w / 1.5, y + h]
                pyautogui.moveTo(point)
                check_mob()
                r += 1
        if k == 11:
            k = 1
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
