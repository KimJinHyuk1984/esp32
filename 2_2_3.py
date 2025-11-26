# 2_2_3.py

from machine import Pin
import time

button_pin = 18

# ✅ 풀업 방식 (GND와 연결된 버튼)
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
prev_state = button.value()

while True:
    current_state = button.value()
    if prev_state != current_state:
        print("click")
    prev_state = current_state
    time.sleep(0.1)