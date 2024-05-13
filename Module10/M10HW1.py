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



