from machine import ADC, Pin, Map # include ADC, Pin and Map functions from machine module
import time # include time module 

adc = ADC(Pin(Map.WIO_MIC)) # create ADC on built-in mic pin 

while True: # while loop
    adc_val = adc.read() # read ADC values (0 ~ 1023)
    print(adc_val) # print ADC values 
    time.sleep_ms(200) # delay

