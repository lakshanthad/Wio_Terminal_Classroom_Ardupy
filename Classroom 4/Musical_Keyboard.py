from machine import Pin, Map, LCD # include Pin, Map and LCD functions from machine module 
import time # include time module 

BUZZER = Pin(Map.WIO_BUZZER, Pin.OUT) # set Buzzer Pin as OUTPUT

# button pin configurations
Button_A = Pin(Map.WIO_KEY_A, Pin.IN) # set button pin as INPUT
Button_B = Pin(Map.WIO_KEY_B, Pin.IN) 
Button_C = Pin(Map.WIO_KEY_C, Pin.IN)

# 5-way switch pin configurations
SWITCH_UP = Pin(Map.WIO_5S_UP, Pin.IN) # set switch pin as INPUT
SWITCH_DOWN = Pin(Map.WIO_5S_DOWN, Pin.IN)  
SWITCH_LEFT = Pin(Map.WIO_5S_LEFT, Pin.IN)  
SWITCH_RIGHT = Pin(Map.WIO_5S_RIGHT, Pin.IN)  
SWITCH_PRESS = Pin(Map.WIO_5S_PRESS, Pin.IN)   

# variables for reading current button/ switch state
Value_Button_A = 0
Value_Button_B = 0
Value_Button_C = 0
Value_SWITCH_UP = 0
Value_SWITCH_DOWN = 0
Value_SWITCH_LEFT = 0
Value_SWITCH_RIGHT = 0
Value_SWITCH_PRESS = 0

# variables for reading previous button/ switch state 
Value_Button_A_OLD = 0
Value_Button_B_OLD = 0
Value_Button_C_OLD = 0
Value_SWITCH_UP_OLD = 0
Value_SWITCH_DOWN_OLD = 0
Value_SWITCH_LEFT_OLD = 0
Value_SWITCH_RIGHT_OLD = 0
Value_SWITCH_PRESS_OLD = 0

lcd = LCD() # TFT LCD initialization

lcd.fillScreen(lcd.color.WHITE) # fill background in white

# # draw lower notes with black border
# lcd.drawRect(0,0,40,240,lcd.color.BLACK) # draw rectangle with black border
# lcd.drawRect(40,0,40,240,lcd.color.BLACK)
# lcd.drawRect(80,0,40,240,lcd.color.BLACK)
# lcd.drawRect(120,0,40,240,lcd.color.BLACK)
# lcd.drawRect(160,0,40,240,lcd.color.BLACK)
# lcd.drawRect(200,0,40,240,lcd.color.BLACK)
# lcd.drawRect(240,0,40,240,lcd.color.BLACK)
# lcd.drawRect(280,0,40,240,lcd.color.BLACK)

# # draw upper notes with black fill
# lcd.fillRect(25,0,30,130,lcd.color.BLACK) # fill rectangle with black 
# lcd.fillRect(65,0,30,130,lcd.color.BLACK)
# lcd.fillRect(145,0,30,130,lcd.color.BLACK)
# lcd.fillRect(185,0,30,130,lcd.color.BLACK)
# lcd.fillRect(225,0,30,130,lcd.color.BLACK)
# lcd.fillRect(305,0,30,130,lcd.color.BLACK)

# # draw for note labels 
# lcd.setTextColor(lcd.color.BLACK) # set text color
# lcd.setTextSize(3) # set text size 
# lcd.drawString("C",15,180) # draw text string
# lcd.drawString("D",55,180) # draw text string
# lcd.drawString("E",95,180) # draw text string
# lcd.drawString("F",135,180) # draw text string
# lcd.drawString("G",175,180) # draw text string
# lcd.drawString("A",215,180) # draw text string
# lcd.drawString("B",255,180) # draw text string
# lcd.drawString("C",295,180) # draw text string

def buzz(frequency): # function to generate buzzer sound with desired frequency 
    cycle = 1000000/ frequency # one time period in microseconds (1s=1000000us)
    half_cycle = int((cycle/2)) # half time period in microseconds
    BUZZER.value(1) # set Buzzer Pin to HIGH 
    time.sleep_us(half_cycle) # first half of the time period 
    BUZZER.value(0) # set Buzzer Pin to LOW
    time.sleep_us(half_cycle) # second half of the time period 

def main(): # main function
    # assign global variables for reading current button/ switch state
    global Value_Button_A 
    global Value_Button_B 
    global Value_Button_C 
    global Value_SWITCH_UP 
    global Value_SWITCH_DOWN 
    global Value_SWITCH_LEFT 
    global Value_SWITCH_RIGHT 
    global Value_SWITCH_PRESS 

    # assign global variables for reading previous button/ switch state
    global Value_Button_A_OLD 
    global Value_Button_B_OLD 
    global Value_Button_C_OLD 
    global Value_SWITCH_UP_OLD 
    global Value_SWITCH_DOWN_OLD 
    global Value_SWITCH_LEFT_OLD 
    global Value_SWITCH_RIGHT_OLD 
    global Value_SWITCH_PRESS_OLD 

    while True: # while loop 
        # assign variables to read current button states (0 or 1)
        Value_Button_A = Button_A.value()
        Value_Button_B = Button_B.value()
        Value_Button_C = Button_C.value()
        Value_SWITCH_UP = SWITCH_UP.value()
        Value_SWITCH_DOWN = SWITCH_DOWN.value()
        Value_SWITCH_LEFT = SWITCH_LEFT.value()
        Value_SWITCH_RIGHT = SWITCH_RIGHT.value()
        Value_SWITCH_PRESS = SWITCH_PRESS.value()

        # Note C
        if (Value_Button_C == 0): # when button C is pressed
            if (Value_Button_C_OLD != Value_Button_C): # debounce input to make sure of button press
                Value_Button_C_OLD = Value_Button_C
                #draw on screen
                lcd.fillRect(0,0,40,240,lcd.color.BLACK) # fill note C in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("C",15,180) # draw text string
            buzz(261) # execute buzz function with 261 as frequency

        else: # when button C is not pressed
            if (Value_Button_C_OLD != Value_Button_C): # debounce input to make sure of button press
                Value_Button_C_OLD = Value_Button_C
                lcd.fillRect(0,0,40,240,lcd.color.WHITE) # fill note C in white
                lcd.drawRect(0,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(25,0,30,130,lcd.color.BLACK) # fill note C# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("C",15,180) # draw text string

        # Note D
        if (Value_Button_B == 0): # when button B is pressed
            if (Value_Button_B_OLD != Value_Button_B): # debounce input to make sure of button press
                Value_Button_B_OLD = Value_Button_B
                #draw on screen
                lcd.fillRect(40,0,40,240,lcd.color.BLACK) # fill note D in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("D",55,180) # draw text string
            buzz(294) # execute buzz function with 294 as frequency

        else: # when button B is not pressed
            if (Value_Button_B_OLD != Value_Button_B): # debounce input to make sure of button press
                Value_Button_B_OLD = Value_Button_B
                lcd.fillRect(40,0,40,240,lcd.color.WHITE) # fill note D in white
                lcd.drawRect(40,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(25,0,30,130,lcd.color.BLACK) # fill note C# in black
                lcd.fillRect(65,0,30,130,lcd.color.BLACK) # fill note D# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("D",55,180) # draw text string

        # Note E
        if (Value_Button_A == 0): # when button A is pressed
            if (Value_Button_A_OLD != Value_Button_A): # debounce input to make sure of button press
                Value_Button_A_OLD = Value_Button_A
                #draw on screen
                lcd.fillRect(80,0,40,240,lcd.color.BLACK) # fill note E in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("E",95,180) # draw text string
            buzz(329) # execute buzz function with 329 as frequency

        else: # when button A is not pressed
            if (Value_Button_A_OLD != Value_Button_A): # debounce input to make sure of button press
                Value_Button_A_OLD = Value_Button_A
                lcd.fillRect(80,0,40,240,lcd.color.WHITE) # fill note E in white
                lcd.drawRect(80,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(65,0,30,130,lcd.color.BLACK) # fill note D# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("E",95,180) # draw text string

        # Note F
        if (Value_SWITCH_LEFT == 0): # when SWITCH_LEFT is pressed
            if (Value_SWITCH_LEFT_OLD != Value_SWITCH_LEFT): # debounce input to make sure of button press
                Value_SWITCH_LEFT_OLD = Value_SWITCH_LEFT
                #draw on screen
                lcd.fillRect(120,0,40,240,lcd.color.BLACK) # fill note F in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("F",135,180) # draw text string
            buzz(349) # execute buzz function with 349 as frequency

        else: # when SWITCH_LEFT is not pressed
            if (Value_SWITCH_LEFT_OLD != Value_SWITCH_LEFT): # debounce input to make sure of button press
                Value_SWITCH_LEFT_OLD = Value_SWITCH_LEFT
                lcd.fillRect(120,0,40,240,lcd.color.WHITE) # fill note F in white
                lcd.drawRect(120,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(145,0,30,130,lcd.color.BLACK) # fill note F# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("F",135,180) # draw text string

        # Note G
        if (Value_SWITCH_RIGHT == 0): # when SWITCH_RIGHT is pressed
            if (Value_SWITCH_RIGHT_OLD != Value_SWITCH_RIGHT): # debounce input to make sure of button press
                Value_SWITCH_RIGHT_OLD = Value_SWITCH_RIGHT
                #draw on screen
                lcd.fillRect(160,0,40,240,lcd.color.BLACK) # fill note G in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("G",175,180) # draw text string
            buzz(392) # execute buzz function with 392 as frequency

        else: # when SWITCH_RIGHT is not pressed
            if (Value_SWITCH_RIGHT_OLD != Value_SWITCH_RIGHT): # debounce input to make sure of button press
                Value_SWITCH_RIGHT_OLD = Value_SWITCH_RIGHT
                lcd.fillRect(160,0,40,240,lcd.color.WHITE) # fill note G in white
                lcd.drawRect(160,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(145,0,30,130,lcd.color.BLACK) # fill note F# in black
                lcd.fillRect(185,0,30,130,lcd.color.BLACK) # fill note G# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("G",175,180) # draw text string

        # Note A
        if (Value_SWITCH_UP == 0): # when SWITCH_UP is pressed
            if (Value_SWITCH_UP_OLD != Value_SWITCH_UP): # debounce input to make sure of button press
                Value_SWITCH_UP_OLD = Value_SWITCH_UP
                #draw on screen
                lcd.fillRect(200,0,40,240,lcd.color.BLACK) # fill note A in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("A",215,180) # draw text string
            buzz(440) # execute buzz function with 440 as frequency

        else: # when SWITCH_UP is not pressed
            if (Value_SWITCH_UP_OLD != Value_SWITCH_UP): # debounce input to make sure of button press
                Value_SWITCH_UP_OLD = Value_SWITCH_UP
                lcd.fillRect(200,0,40,240,lcd.color.WHITE) # fill note A in white
                lcd.drawRect(200,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(185,0,30,130,lcd.color.BLACK) # fill note G# in black
                lcd.fillRect(225,0,30,130,lcd.color.BLACK) # fill note A# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("A",215,180) # draw text string

        # Note B
        if (Value_SWITCH_DOWN == 0): # when SWITCH_DOWN is pressed
            if (Value_SWITCH_DOWN_OLD != Value_SWITCH_DOWN): # debounce input to make sure of button press
                Value_SWITCH_DOWN_OLD = Value_SWITCH_DOWN
                #draw on screen
                lcd.fillRect(240,0,40,240,lcd.color.BLACK) # fill note B in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("B",255,180) # draw text string
            buzz(493) # execute buzz function with 493 as frequency

        else: # when SWITCH_DOWN is not pressed
            if (Value_SWITCH_DOWN_OLD != Value_SWITCH_DOWN): # debounce input to make sure of button press
                Value_SWITCH_DOWN_OLD = Value_SWITCH_DOWN
                lcd.fillRect(240,0,40,240,lcd.color.WHITE) # fill note B in white
                lcd.drawRect(240,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(225,0,30,130,lcd.color.BLACK) # fill note A# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("B",255,180) # draw text string

        # Note Upper C
        if (Value_SWITCH_PRESS == 0): # when SWITCH_PRESS is pressed
            if (Value_SWITCH_PRESS_OLD != Value_SWITCH_PRESS): # debounce input to make sure of button press
                Value_SWITCH_PRESS_OLD = Value_SWITCH_PRESS
                #draw on screen
                lcd.fillRect(280,0,40,240,lcd.color.BLACK) # fill note c in black when pressed
                lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK) # white text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("C",295,180) # draw text string
            buzz(523) # execute buzz function with 523 as frequency

        else: # when SWITCH_PRESS is not pressed
            if (Value_SWITCH_PRESS_OLD != Value_SWITCH_PRESS): # debounce input to make sure of button press
                Value_SWITCH_PRESS_OLD = Value_SWITCH_PRESS
                lcd.fillRect(280,0,40,240,lcd.color.WHITE) # fill note C in white
                lcd.drawRect(280,0,40,240,lcd.color.BLACK) # draw note black border
                lcd.fillRect(305,0,30,130,lcd.color.BLACK) # fill note C# in black
                lcd.setTextColor(lcd.color.BLACK, lcd.color.WHITE) # black text
                lcd.setTextSize(3) # set text size 
                lcd.drawString("C",295,180) # draw text string

if __name__ == "__main__": # checks whether this is run from main.py
    main() # execute function