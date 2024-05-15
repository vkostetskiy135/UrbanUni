import time
from threading import Thread


def number_print():
    for n in range(1, 11):
        print(n, flush=True)
        time.sleep(1)


def letter_print():
    letters = 'abcdefghij'
    for l in letters:
        print(l, flush=True)
        time.sleep(1)


thread = Thread(target=number_print)
thread.start()
time.sleep(0.5)
thread = Thread(target=letter_print())
thread.start()

