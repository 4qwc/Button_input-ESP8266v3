# basic INPUT

from machine import Pin
import time

btn1 = 2
button1 = Pin(btn1, Pin.IN, Pin.PULL_UP) # set input pin

RLPIN_1 = 4 #output pin GPIO 4
relay_1 = Pin(RLPIN_1, Pin.OUT)#output pin

ON = 0
OFF = 1

relay_1.value(OFF)# set defult OFF

def turn_on():
    relay_1.value(ON)
    print("RELAY - ON ")
    
def turn_off():
    relay_1.value(OFF)
    print("RELAY- OFF")
    

while True:
    SW =  button1.value()
    time.sleep(0.01)
    F_SW = button1.value()
    
    if SW and not F_SW:
        turn_on()
        print("กดปุ่ม เปิดรีเลย์!")
    elif not SW and F_SW:
        turn_off()
        print("ปล่อย ดับ!")
    
    

    