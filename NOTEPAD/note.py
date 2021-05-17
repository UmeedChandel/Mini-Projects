from tkinter import *                    # toolkit for GUI interface
from tkinter.filedialog import *         # file selection dialogs module
import tkinter as tk                     # as alias tk

note = tk.Tk()                      # creating GUI
note.title("Notepad")               # title for GUI

w= note.winfo_screenwidth()         # retriving window info for width
h= note.winfo_screenheight()        # retriving window info for height

note.geometry("%dx%d+0+0" % (w/2,h/2))   # place the half window size
note.config(bg = "white")                # set background color
top = Frame(note)
top.pack(padx = 10, pady = 5, anchor = 'nw')

def saveFile():         #save file function write mode
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(padSpace.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():         #open file function read mode
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    padSpace.insert(INSERT, content)

def clearFile():        #clear file function from start to end
    padSpace.delete(1.0, END)

def switchModeD():      # switch to dark mode
    note.config(bg="#000000")
    padSpace.config(bg = "#1F1F1F",foreground= "white")

def switchModeL():      # switch to light mode
    note.config(bg="white")
    padSpace.config(bg = "#F2F2F8",foreground= "#000000")

b1 = Button(note, text="Open", bg = "#000000",foreground= "white",borderwidth="3", command = openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(note, text="Save", bg = "#000000",foreground= "white",borderwidth="3", command = saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(note, text="Clear", bg = "#000000",foreground= "white",borderwidth="3", command = clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(note, text="Exit", bg = "#000000",foreground= "white",borderwidth="3", command = exit)
b4.pack(in_ = top, side=LEFT)

b4 = Button(note, text="Dark", bg = "#000000",foreground= "white",borderwidth="3", command = switchModeD)
b4.pack(in_ = top, side=LEFT)

b5 = Button(note, text="Light", bg = "#000000",foreground= "white",borderwidth="3", command = switchModeL)
b5.pack(in_ = top, side=LEFT)

padSpace = Text(note, wrap = WORD, bg = "#F2F2F8", font = ("poppins", 15))
padSpace.pack(padx = 10, pady = 10, expand = TRUE, fill = BOTH)

note.mainloop()         # looping