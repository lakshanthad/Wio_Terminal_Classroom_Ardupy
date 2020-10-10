from machine import ADC, Pin, Map # include ADC, Pin and Map functions from machine module
import time # include time module 

WINDOW_SIZE = 50 # amount of previous signal entries that can be averaged together

# set variables to 0
INDEX = 0 
VALUE = 0
SUM = 0
AVERAGED = 0
dB = 0
READINGS = [0]*WINDOW_SIZE 

adc = ADC(Pin(Map.WIO_MIC)) # create ADC on built-in mic pin 

def main(): # create function
    global INDEX, VALUE, SUM, AVERAGED, dB, READINGS # make variables as global
    SUM = SUM - READINGS[INDEX] # Remove the oldest entry from the sum      
    VALUE = adc.read() # Read ADC values 
    READINGS[INDEX] = VALUE # Add the newest reading to the window     
    SUM = SUM + VALUE # Add the newest reading to the sum
    INDEX = (INDEX+1) % WINDOW_SIZE # Increment the index, and wrap to 0 if it exceeds the window size 

    AVERAGED = SUM / WINDOW_SIZE # Equation for the result 

    print(VALUE, end=" ") # print ADC values 

    print(AVERAGED) # print values after filter 

    time.sleep_ms(100) # delay 
    
if __name__ == "__main__": # checks whether this is run from main.py
    while True: # while loop
        main() # execute function
