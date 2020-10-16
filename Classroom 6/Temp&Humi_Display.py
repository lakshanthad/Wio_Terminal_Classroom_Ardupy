from arduino import grove_dht
from machine import LCD, Sprite
import time 

dht = grove_dht(0,11)
lcd = LCD() # initialize TFT LCD 
spr = Sprite(lcd) # initialize buffer

def main(): # main function 
    spr.createSprite(320, 240) # create buffer
    while True: # while loop
        spr.fillSprite(spr.color.WHITE) # fill background 

        # two fill rectangles
        spr.fillRect(0,0,160,240,spr.color.DARKGREEN) # fill rectangle in color
        spr.fillRect(160,0,160,240,spr.color.BLUE)

        # temp and humid text draw 
        spr.setTextSize(2) # set text size
        spr.setTextColor(spr.color.WHITE,spr.color.DARKGREEN) # set text color
        spr.drawString("Temperature", 15, 65) # draw string 
        spr.setTextColor(spr.color.WHITE,spr.color.BLUE) 
        spr.drawString("Humidity", 190, 65) 

        # obtain readings 
        t = dht.temperature # store temperature readings in variable 
        h = dht.humidity # store humidity readings in variable 
        
        # display temp readings
        spr.setTextSize(4)
        spr.setTextColor(spr.color.WHITE,spr.color.DARKGREEN)
        spr.drawNumber(int(t),50,110) # display number  
        spr.drawString("C", 100, 110) 

        # display humi readings
        spr.setTextColor(spr.color.WHITE,spr.color.BLUE) # set text color
        spr.drawNumber(int(h),180,110)  
        spr.drawString("%RH", 235, 110) 

        spr.pushSprite(0,0) # push to LCD
        time.sleep_ms(100)


 
if __name__ == "__main__": # check whether this is run from main.py
    main() # execute function
