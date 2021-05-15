import tkinter as tk		# toolkit for GUI interface
from tkinter.ttk import *	# module for Tk themed widget set
from time import strftime	# string from time that returns formatted string

root = tk.Tk()	            # creating GUI
root.title("TIME")	        # title for GUI

w= root.winfo_screenwidth()         # retriving window info for width
h= root.winfo_screenheight()	    # retriving window info for height
root.configure(bg='black')          # set background color
root.geometry("%dx%d+0+0" % (w,h))  # place the window fullscreen size

def Time():
    txt = strftime('%I:%M:%S %p')	# format of time
    label.config(text=txt)           # set time to lable
    label.after(1000, Time)             # calling time function every 1 second

label = tk.Label(root, font=("ds-digital",200), background="black", foreground="white",padx=w/2-20,pady=h/2-20)    # lable to store our clock
label.pack()	                                                                                                   # packing the label
Time() 	                                                                                                           # calling time function

root.mainloop()                                                                                                    # looping