from machine import Pin, Map # include Pin and Map functions from machine module 
import time # import time module 

# assign variables for PWM
frequency = 1000 # PWM frequency 
cycle = 1000000/ frequency # one time period in microseconds (1s=1000000us)
half_cycle = int((cycle/2)) # half time period in microseconds 

BUZZER = Pin(Map.WIO_BUZZER, Pin.OUT) # set Buzzer Pin as OUTPUT

def main(): # main function 
    BUZZER.value(1) # set Buzzer Pin to HIGH 
    time.sleep_us(half_cycle) # first half of the time period   
    BUZZER.value(0) # set Buzzer Pin to LOW
    time.sleep_us(half_cycle) # second half of the time period

if __name__ == "__main__": # checks whether this is run from main.py 
    while True: # while True 
        main() # execute function 






