# 2_1_2.py
# 3색 LED 깜빡이기

from machine import Pin
import time

# 핀 번호 지정
red_pin = 4
yellow_pin = 5
blue_pin = 21

# LED 핀 모드 설정
red = Pin(red_pin, Pin.OUT)
yellow = Pin(yellow_pin, Pin.OUT)
blue = Pin(blue_pin, Pin.OUT)

# LED를 깜빡이는 코드 작성
while True:
    red.value(1)
    time.sleep(0.5)
    yellow.value(1)
    time.sleep(0.5)
    blue.value(1)
    time.sleep(0.5)
    
    red.value(0)
    time.sleep(0.5)
    yellow.value(0)
    time.sleep(0.5)
    blue.value(0)
    time.sleep(0.5)