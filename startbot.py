import threading
from tp import start_tp
from usebaf import baf
from main import start
import time
from CheckHP import checkHP
from win32api import keybd_event


def my_hp():
    while True:
        hp = checkHP()[:4]
        try:
            if hp.isdigit():
                hp = int(checkHP())
                print('hp = ', hp)
                if hp <= 1100:
                    sema.acquire()
                    keybd_event(0x71, 0, 0, 0)  # tp f2
                    time.sleep(2)
                    keybd_event(0x76, 0, 0, 0)  # m_orf
                    time.sleep(1)
                    keybd_event(0x77, 0, 0, 0)  # f8
                    time.sleep(6)
                    sema.release()
                elif 1100 < hp <= 1600:
                    keybd_event(0x77, 0, 0, 0)  # f8
        except ValueError:
            pass


def start_farm():  # main
    start()


def use_tp(tp=1):  # func_b
    sema.acquire()
    sema.release()
    start_tp(tp)


def start_baf():  # +++  func_c
    t = 0
    while True:
        sema.acquire()
        sema.release()
        t += 1
        baf(t)


sema = threading.Semaphore()

thread_check = threading.Thread(target=my_hp)
thread_tp = threading.Thread(target=use_tp)
thread_farm = threading.Thread(target=start_farm)
thread_baf = threading.Thread(target=start_baf)

thread_check.start()
thread_farm.start()
thread_baf.start()
