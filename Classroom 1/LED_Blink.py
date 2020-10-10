from machine import Pin, Map #include Pin and Map functions from machine module 
import time #include time module 
 
LED = Pin(Map.LED_BUILTIN, Pin.OUT) #Set built-in LED as an OUTPUT
 
while True: #while loop
    LED.on() #turn the built-in LED on
    time.sleep(1) #delay for 1 second
    LED.off() #turn the LED off
    time.sleep(1) #delay for 1 second