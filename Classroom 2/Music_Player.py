from machine import LCD #include LCD function from machine module
 
lcd = LCD() #initialize TFT LCD 

lcd.fillScreen(lcd.color.WHITE) #fill background color 
lcd.setRotation(3) #set screen rotation 

#draw for title header
lcd.fillRect(0,0,320,60,lcd.color.DARKGREEN) #draw rectangle with border
lcd.setTextSize(3) #set text size 
lcd.setTextColor(lcd.color.WHITE,lcd.color.DARKGREEN) #color of text 
lcd.drawString("MUSIC PLAYER",55,15) #draw a string

#draw for volume 
lcd.drawRoundRect(90,75,140,60,15,lcd.color.BLUE) #draw round corner rectangle with border
lcd.fillTriangle(40,105,80,75,80,135,lcd.color.RED) #draw triangle with fill color
lcd.fillTriangle(280,105,240,75,240,135,lcd.color.DARKGREEN)
lcd.setTextColor(lcd.color.BLACK)
lcd.drawString("VOLUME",105,95)

#draw for play
lcd.drawCircle(160,190,45,lcd.color.BLUE) #draw circle with fill color
lcd.fillTriangle(60,185,100,155,100,215,lcd.color.RED)
lcd.fillTriangle(260,185,220,155,220,215,lcd.color.DARKGREEN)
lcd.drawString("PLAY",130,180)
