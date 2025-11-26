# 2_2_4.py

from machine import Pin
import time

button_pin = 18
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)

prev_state = button.value()

def get_key():
    global prev_state
    current_state = button.value()
    if prev_state != current_state:
        prev_state = current_state
        if current_state == 0:
            return 1
    else:
        return 0
    
while True:
    if get_key():
        print("click")
        time.sleep(0.1)
