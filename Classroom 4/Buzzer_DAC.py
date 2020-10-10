from machine import Pin, Map, DAC # include Pin, Map and DAC from machine module 
import time # import time module

BUZZER = DAC(Pin(Map.WIO_BUZZER)) # create DAC on WIO BUZZER Pin

BUZZER.write(180) # write value to DAC, 180/4096*3.3 = 0.145V





