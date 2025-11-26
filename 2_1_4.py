# 2_1_4.py

from machine import Pin
import time

# 핀 번호 지정을 위한 리스트 만들기
led_pins = [4, 5, 21]
leds = []

# 핀 모드 설정
for pin in led_pins:
	leds.append(Pin(pin, Pin.OUT))
	
# LED OFF로 초기화
for led in leds:
	led.value(0)

# 키보드 인터럽트 설정
try:
	# 무한 루프
	while True:
		for led in leds:
				led.value(1)
				time.sleep(0.5)
		
		for led in leds:
				led.value(0)
				time.sleep(0.5)

except KeyboardInterrupt:
	for led in leds:
			led.value(0)
print("코드를 종료합니다.")