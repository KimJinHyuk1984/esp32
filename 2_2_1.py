# 2_2_1.py

from machine import Pin
import time

button_pin = 18

# ✅ 풀업 방식 (GND와 연결된 버튼)
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

while True:
    state = button.value()
    print(state)  # 눌렸을 때 0, 떼었을 때 1
    time.sleep(0.1)