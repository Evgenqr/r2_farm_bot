import threading
import time
from CheckHP import checkHP
from win32api import keybd_event


def my_hp():
    k = 0
    while True:
        hp = checkHP()[:4]
        try:
            if hp.isdigit():
                hp = int(checkHP())
                print('hp = ', hp)
                if hp <= 1340:
                    print('tp(51) and hill(71) and use morf(76)')
                    lock_farm.acquire()
                    keybd_event(0x71, 0, 0, 0)  # tp f2
                    time.sleep(2)
                    keybd_event(0x76, 0, 0, 0)  # morf
                    time.sleep(1)
                    keybd_event(0x77, 0, 0, 0)  # f8
                    time.sleep(6)
                    lock_farm.release()
                elif 1340 < hp <= 1544:
                    print('farm and hill(71)')
                    keybd_event(0x77, 0, 0, 0)  # f8
                elif hp > 1544:
                    print('farm  ====', k)
                    k += 1
                    # start()
        except ValueError:
            pass


def farm():
    time.sleep(1)
    while True:
        lock_farm.acquire()
        lock_farm.release()
        time.sleep(1.5)


lock_check = threading.Lock()
lock_farm = threading.Lock()

thread1 = threading.Thread(target=my_hp)
thread2 = threading.Thread(target=farm)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
