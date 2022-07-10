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

#version2
btn1_pin = board.GP15
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

minDelay = 180; maxDelay = 300
minDist = -3; maxDist = 3

def getRandom(min,max):
    return (random.randint(min,max))

for i in range(4):
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.1)
#time.sleep(300)
    
last_state = False
curr_state = False
state = 0
x = 0

while True:
    curr_state = btn1.value
    if last_state == 1 and curr_state == 0:
        if state == 0:
            state = 1
        elif state == 1:
            state = 0
    last_state = curr_state
    x = x+1
    if state == 0:
        led.value = False
        #if (x/2) == 0:
            #print("State 0: Idle")
    elif state == 1:
        led.value = True
        #if (x/2) == 0:
            #print("State 1: Jiggling")
        #mouse.move(getRandom(minDist,maxDist), getRandom(minDist,maxDist))
        R = random.randint(0,10) #radius
        x = getRandom(minDist,maxDist)
        y = getRandom(minDist,maxDist)
        for k in range(501):
            #print(k)
            if k == 500:
               # print("11111111!!!")
                for i in range(random.randint(0,360)):
                    if i%6==0:
                        circlex = int(R*math.cos(math.radians(i)))
                        circley = int(R*math.sin(math.radians(i)))
                        #for i in range(random.randint(0,10)):
                        mouse.move(x + circlex,y + circley)
                        for j in range(random.randint(0,1000)):
                            time.sleep(.00000000001)
                            if btn1.value == True:
                                print("leave")
                                break
                        #mouse.move(1,0)
                        scroll = random.randint(0,100)
                        if scroll < 90:
                            continue
                        elif scroll > 95:
                            mouse.move(wheel=-1)
                        elif scroll :
                            mouse.move(wheel=1)
                #for i in range(getRandom(minDelay,maxDelay)):
            else:
                for j in range(1000):
                    time.sleep(.00000000001)
                    if btn1.value == True:
                        #print("leave")
                        break



        


