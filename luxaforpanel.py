import luxafor
import time
from Tkinter import *

class Application(Frame):

    def createWidgets(self):
        self.tickImg = PhotoImage(file="checkmark.gif")
        self.crossImg = PhotoImage(file="cross.gif")
        self.offImg = PhotoImage(file="switch.gif")

        self.OK = Button(self)
        self.OK["text"] = "Ok"
        self.OK["fg"]   = "GREEN"
        self.OK["command"] =  lambda: luxafor.fadeRGB(0,255,0)
        self.OK["image"] = self.tickImg

        self.OK.pack({"side": "left"})

        self.BUSY = Button(self)
        self.BUSY["text"] = "Busy"
        self.BUSY["fg"]   = "RED"
        self.BUSY["command"] =  lambda: luxafor.fadeRGB(255,0,0)
        self.BUSY["image"] = self.crossImg

        self.BUSY.pack({"side": "left"})

        self.OFF = Button(self)
        self.OFF["text"] = "Off"
        self.OFF["fg"]   = "BLACK"
        self.OFF["command"] =  lambda: luxafor.fadeRGB(0,0,0)
        self.OFF["image"] = self.offImg

        self.OFF.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# initialise device
luxafor.initialise()

# create root and set to show above other windows
root = Tk()
root.title('LuxPanel')
root.wm_attributes("-topmost", 1)

# start application
app = Application(master=root)
app.mainloop()

# turn off luxafor on close
luxafor.setLuxaforColor(79)