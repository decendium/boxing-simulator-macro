# lmao
import time as t 
import pynput
from pynput.keyboard import Key, Controller

keyboard = Contoller()
def main():
    a = True
    keyboard.press('w')
    t.sleep(1)
    keyboard.release('w')
    keyboard.press('s')
    t.sleep(2)
    keyboard.release('s')
    while a is True:
        keyboard.press('w')
        t.sleep(2)
        keyboard.release('w')
        keyboard.press('s')
        t.sleep(2)
        keyboard.release('s')


main()