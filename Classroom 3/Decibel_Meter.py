from machine import ADC, Pin, Map, LCD, Sprite  # include ADC, Pin, Map, LCD and Sprite functions from machine module
import time, math # include time and math module 

adc = ADC(Pin(Map.WIO_MIC)) # create ADC on built-in Mic Pin 

WINDOW_SIZE = 50 # amount of previous signal entries that can be averaged together

# set variables to 0
INDEX = 0 
VALUE = 0
SUM = 0
AVERAGED = 0
READINGS = [0]*WINDOW_SIZE 
dB = 0

tft = LCD() # LCD initialization
tft.setRotation(3) # set screen rotation 
spr = Sprite(tft) # initialize buffer 
spr.createSprite(320,75) # create buffer

ltx = 0 # saved x coordinate of bottom of needle 
osx = 160 # saved x coordinate 
osy = 160 # saved y coordinate
updateTime = 0 # time for next update

# create function to draw all graphics on LCD
def analogMeter():
    tft.fillScreen(tft.color.YELLOW) # set background color
    tft.fillRect(5,3,310,158,tft.color.WHITE) # set meter box color 
    tft.drawRect(5,3,310,158,tft.color.BLACK) # draw border line 

    tft.setTextColor(tft.color.BLACK) # set text color

    # draw ticks every 5 degrees from -50 to +50 degrees 
    for i in range(-50,51,5):
        # long scale tick length 
        tl = 20

        # coordinates of tick to draw 
        sx = math.cos((i - 90) * 0.0174532925)
        sy = math.sin((i - 90) * 0.0174532925)
        x0 = sx * (133 + tl) + 160
        y0 = sy * (133 + tl) + 186
        x1 = sx * 133 + 160
        y1 = sy * 133 + 186

        # coordinates of next tick for zone fill
        sx2 = math.cos((i + 5 - 90) * 0.0174532925)
        sy2 = math.sin((i + 5 - 90) * 0.0174532925)
        x2 = sx2 * (133 + tl) + 160
        y2 = sy2 * (133 + tl) + 186
        x3 = sx2 * 133 + 160
        y3 = sy2 * 133 + 186 

        # Green zone limits 
        if (i >= -50 and i < 0):
            tft.fillTriangle(int(x0), int(y0), int(x1), int(y1), int(x2), int(y2), tft.color.GREEN)
            tft.fillTriangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), tft.color.GREEN)
        # Yellow zone limits 
        if (i >= 0 and i < 25):
            tft.fillTriangle(int(x0), int(y0), int(x1), int(y1), int(x2), int(y2), tft.color.YELLOW)
            tft.fillTriangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), tft.color.YELLOW)

        # Red zone limits
        if (i >= 25 and i < 50):
            tft.fillTriangle(int(x0), int(y0), int(x1), int(y1), int(x2), int(y2), tft.color.RED)
            tft.fillTriangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), tft.color.RED)

        # short scale tick length 
        if (i % 25 != 0):
            tl = 8

        # recalculate coordinates incase tick length has changed 
        x0 = sx * (133 + tl) + 160
        y0 = sy * (133 + tl) + 186
        x1 = sx * 133 + 160
        y1 = sy * 133 + 186 

        # draw ticks 
        tft.drawLine(int(x0), int(y0), int(x1), int(y1), tft.color.BLACK)

        # find positions for labels 
        if (i % 25 == 0):
            x0 = sx * (133 + tl + 10) + 160
            y0 = sy * (133 + tl + 10) + 186

        # draw labels as numbers for 0, 25, 50, 75 and 100
        if (i/25 == -2):
            tft.drawCentreString("0", int(x0), int(y0) - 12, 2)
        elif (i/25 == -1):
            tft.drawCentreString("25", int(x0), int(y0) - 9, 2)
        elif (i/25 == -0):
            tft.drawCentreString("50", int(x0), int(y0) - 7, 2)
        elif (i/25 == 1):
            tft.drawCentreString("75", int(x0), int(y0) - 9, 2)
        elif (i/25 == 2):
            tft.drawCentreString("100", int(x0), int(y0) - 12, 2)


def digitalMeter(): # create function
    global INDEX, VALUE, SUM, AVERAGED, READINGS, dB # make variables as global
    SUM = SUM - READINGS[INDEX] # Remove the oldest entry from the sum      
    VALUE = adc.read() # Read ADC values 
    READINGS[INDEX] = VALUE # Add the newest reading to the window     
    SUM = SUM + VALUE # Add the newest reading to the sum
    INDEX = (INDEX+1) % WINDOW_SIZE # Increment the index, and wrap to 0 if it exceeds the window size 

    AVERAGED = SUM / WINDOW_SIZE # Equation for the result 

    dB = (AVERAGED - 425.77) / 3.19 # equation for dB

    spr.fillSprite(spr.color.YELLOW) # fill sprite in yellow 
    spr.setTextColor(spr.color.BLACK) # set text color 
    spr.setTextSize(4) # set text size 
    spr.drawFloat(dB,1,83,20) # draw float 
    spr.drawString("dB",208,20) # draw a string 
    spr.pushSprite(0,165) # push to LCD 
    time.sleep_ms(25) # delay

# function to map ADC values to 0 ~ 1023 
def mapto(x,a,b,c,d):
    y=(x-a)/(b-a)*(d-c)+c
    return y

# function to move the needle 
def plotNeedle():
    global INDEX, VALUE, SUM, AVERAGED, READINGS, dB # make variables as global
    SUM = SUM - READINGS[INDEX] # Remove the oldest entry from the sum      
    VALUE = adc.read() # Read ADC values 
    READINGS[INDEX] = VALUE # Add the newest reading to the window     
    SUM = SUM + VALUE # Add the newest reading to the sum
    INDEX = (INDEX+1) % WINDOW_SIZE # Increment the index, and wrap to 0 if it exceeds the window size 

    AVERAGED = SUM / WINDOW_SIZE # Equation for the result 

    dB = (AVERAGED - 425.77) / 3.19 # equation for dB

    # limit needle stopping points 
    if (dB < 33):
        dB = 33
    if (dB > 100):
        dB = 100 

    time.sleep_ms(250)

    global osx, osy, ltx # assign as global variables 
    tft.setTextColor(tft.color.BLACK, tft.color.WHITE)

    sdeg = mapto(dB,0,100,-140,-40) # map dB values to angle 

    # calculate tip of needle coordinates 
    sx = math.cos(sdeg * 0.0174532925)
    sy = math.sin(sdeg * 0.0174532925)

    # calculate x delta of needle start (does not start at pivot point)
    tx = math.tan((sdeg + 90) * 0.0174532925)

    # erase old needle image 
    tft.drawLine(int(1.33 * (120 + 20 * ltx -1)), int(1.33 * (140 - 20)), int(osx - 1), int(osy), tft.color.WHITE)
    tft.drawLine(int(1.33 * (120 + 20 * ltx)), int(1.33 * (140 - 20)), int(osx), int(osy), tft.color.WHITE)
    tft.drawLine(int(1.33 * (120 + 20 * ltx + 1)), int(1.33 * (140 - 20)), int(osx + 1), int(osy), tft.color.WHITE)

    # replot text under needle 
    tft.setTextColor(tft.color.BLACK)
    tft.drawString("dB",145,90,4)

    # store new needle end coordinates for next erase 
    ltx = tx 
    osx = 130 * sx + 160 
    osy = 130 * sy + 186

    # draw the needle in the new position, magenta makes needle a bit bolder 
    # draws 3 lines to thicken needle 
    tft.drawLine(int(1.33 * (120 + 20 * ltx -1)), int(1.33 * (140 - 20)), int(osx - 1), int(osy), tft.color.RED)
    tft.drawLine(int(1.33 * (120 + 20 * ltx)), int(1.33 * (140 - 20)), int(osx), int(osy), tft.color.MAGENTA)
    tft.drawLine(int(1.33 * (120 + 20 * ltx + 1)), int(1.33 * (140 - 20)), int(osx + 1), int(osy), tft.color.RED)

def initial():
    analogMeter()
    updateTime = time.ticks_ms() # millisecond counter 

def main():
    global updateTime
    if (updateTime <= time.ticks_ms()):
        updateTime = time.ticks_ms() + 35 # update every 35 milliseconds

        plotNeedle()
        digitalMeter()    
    

if __name__ == "__main__": # checks whether this is run from main.py
    initial()
    while True: # while loop
        main() # execute function
