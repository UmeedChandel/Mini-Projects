import tkinter as tk            # toolkit for GUI interface
import time, pyttsx3            # ppttsx3 python text to speech lib offline
from tkinter.ttk import *       # module for Tk themed widget set
from time import strftime       # string from time that returns formatted string
from datetime import datetime   # date and time as human read lib

root = tk.Tk()              # creating GUI
root.title("TIME")          # title for GUI

w= root.winfo_screenwidth()         # retriving window info for width
h= root.winfo_screenheight()        # retriving window info for height
root.configure(bg='black')          # set background color
root.geometry("%dx%d+0+0" % (w,h))  # place the window fullscreen size

def Time():
    txt = strftime('%I:%M:%S %p')   # format of time
    label.config(text=txt)          # set time to lable
    label.after(1000, Time)         # calling time function every 1 second

label = tk.Label(root, font=("ds-digital",200), background="black", foreground="white",padx=w/2-20,pady=h/2-20)    # lable to store our clock
label.pack()                                                                                                       # packing the label
Time()                                                                                                             # calling time function

root.mainloop()                                                                                                     # looping

T = {                                                               # all the hours in a day dictionary T           
  1: "01:00",2: "02:00",3: "03:00",4: "04:00",
  5: "05:00",6: "06:00",7: "07:00",8: "08:00",
  9: "09:00",10: "10:00",11: "11:00",12: "12:00",
}

while True:                                                         # started a loop
    Trn=datetime.now().strftime("%I:%M")                            # storing time right now in Trn
    time.sleep(1)                                                   # sleep the program for about 1 sec
    for i in T:                                                     # traversing through dict T
        if T[i]==Trn:
            engine=pyttsx3.init()                               # creating engine for voice mode
            engine.say("The time is"+datetime.now().strftime("%I")+"o'clock"+"make every minute count.")    # setting the voice
            engine.runAndWait()
            break
    break
