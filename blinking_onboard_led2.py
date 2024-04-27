#This program will blink the onboard LED 10 times in 1 second intervals. 

from machine import Pin
from time import sleep
led_onboard = Pin("LED", Pin.OUT)

turns = 10
while turns > 0:
    led_onboard.value(1)
    sleep(1)
    led_onboard.value(0)
    sleep(1)
    turns -= 1
    print(turns)
