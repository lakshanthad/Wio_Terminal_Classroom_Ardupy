from arduino import grove_ultra_ranger # include ultrasonic distance sensor library 
from machine import LCD, Sprite # include LCD and Sprite functions from machine module
import time # include time module 
 
Ultrasonic = grove_ultra_ranger(0) # set D0 as sensor pin 
lcd = LCD() # initialize TFT LCD 
spr = Sprite(lcd) # initialize buffer
 
def main(): # main function 
    spr.createSprite(320, 240) # create buffer
    while True: # while loop
        spr.fillSprite(spr.color.WHITE) # fill background 

        # header title 
        spr.fillRect(0,0,320,50,spr.color.BLUE) # fill rectangle 
        spr.setTextSize(2) # set text size
        spr.setTextColor(spr.color.WHITE, spr.color.BLUE) # set text color
        spr.drawString("Distance to Object", 55, 15) # draw string 

        spr.drawFastVLine(160,0,240,spr.color.BLUE) # draw verticle line 

        # cm and .in text 
        spr.setTextColor(spr.color.WHITE, spr.color.BLUE)
        spr.setTextSize(4)
        spr.fillRoundRect(50,145,65,50,10,spr.color.BLUE) # fill round rectangle
        spr.fillRoundRect(195,145,85,50,10,spr.color.BLUE)
        spr.drawString("cm", 60, 155) 
        spr.drawString("in.", 205, 155)

        # display cm and .in values 
        spr.setTextColor(spr.color.BLACK)
        spr.drawNumber(Ultrasonic.cm, 60,90) # obtain distance in centimeters and display 
        time.sleep_ms(50) # Needed for data to be read again
        spr.drawNumber(Ultrasonic.inch, 210,90) # obtain distance in inches and display
        
        spr.pushSprite(0,0) # push to LCD
        time.sleep_ms(100) # delay 
 
if __name__ == "__main__": # check whether this is run from main.py
    main() # execute function
