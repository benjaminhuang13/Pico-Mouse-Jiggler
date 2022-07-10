# No button, auto runs when plugged in

import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio
import random
import math

mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

minDelay = 0; maxDelay = 20
minDist = -9; maxDist = 9

def getRandom(min,max):
    return (random.randint(min,max))
time.sleep(10)
while True:
    led.value = True
    #mouse.move(getRandom(minDist,maxDist), getRandom(minDist,maxDist))
    R = random.randint(0,60) #radius
    x = getRandom(minDist,maxDist)
    y = getRandom(minDist,maxDist)
    for i in range(random.randint(0,360)):
        if i%6==0:
            circlex = int(R*math.cos(math.radians(i)))
            circley = int(R*math.sin(math.radians(i)))
            mouse.move(x + circlex,y + circley)
    led.value = False
    time.sleep(getRandom(minDelay,maxDelay))

    


