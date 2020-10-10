from machine import Pin, Map, PWM # include Pin, Map and PWM functions from machine module 
import time # include time module 

# create PWM on WIO BUZZER with 2000Hz frequency and 250 duty cycle 
BUZZER = PWM(Pin(Map.WIO_BUZZER), freq=1000, duty=250)

