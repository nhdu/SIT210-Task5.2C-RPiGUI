from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led_RED = LED(26)
led_BLUE = LED(19)
led_GREEN = LED(13)

## GUI_DEFINITION ##
win = Tk()
win.title("LED_TOGGLER")
my_font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

##EVENT FUNCTION
def offRED():
    led_RED.off()
    ledButton["text"] = "Turn On"
def offBLUE():
    led_BLUE.off()
    ledButton3["text"] = "Turn On"
def offGREEN():
    led_GREEN.off()
    ledButton2["text"] = "Turn On"
def ledRED():
    if led_RED.is_lit:
        led_RED.off()
        ledButton["text"] = "Turn On"
    else:
        led_RED.on()
       
        ledButton["text"] = "Turn Off"

def ledGREEN():
    if led_GREEN.is_lit:
        led_GREEN.off()
        ledButton2["text"] = "Turn On"
    else:
        led_GREEN.on()
       
        ledButton2["text"] = "Turn Off"
        
def ledBLUE():
    if led_BLUE.is_lit:
        led_BLUE.off()
        ledButton3["text"] = "Turn On"
    else:
        led_BLUE.on()
        ledButton3["text"] = "Turn Off"
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        
## WIDGETS ###
label = Label(win, text = "RED LED", font = my_font, bg = "red", height = 1, width = 24)
label.grid(row = 0, column = 1)
ledButton = Button(win, text = "Turn On", font = my_font, command = lambda:[ledRED(), offBLUE(), offGREEN()], bg = "bisque2", height = 1, width =24)
ledButton.grid(row = 1, column = 1)

label = Label(win, text = "BLUE LED", font = my_font, bg = "blue", height = 1, width = 24)
label.grid(row = 3, column = 1)
ledButton3 = Button(win, text = "Turn On", font = my_font, command = lambda:[ledBLUE(), offRED(), offGREEN() ] , bg = "bisque2", height = 1, width =24)
ledButton3.grid(row = 4, column = 1)



label = Label(win, text = "GREEN LED", font = my_font, bg = "green", height = 1, width = 24)
label.grid(row = 6, column = 1)
ledButton2 = Button(win, text = "Turn On", font = my_font, command = lambda:[ledGREEN(), offRED(), offBLUE()], bg = "bisque2", height = 1, width =24)
ledButton2.grid(row = 7, column = 1)


exitButton = Button(win, text = "Exit", font = my_font, command = close, bg = "Grey", height = 1, width =24)
exitButton.grid(row = 8, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
