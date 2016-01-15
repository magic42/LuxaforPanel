import luxafor
import time, subprocess, os
import ConfigParser
from Tkinter import *

class Application(Frame):

    def createWidgets(self):
        config = self.config

        self.OKImg = PhotoImage(file=config.get('OK_Button', 'image'))
        self.BUSYImage = PhotoImage(file=config.get('BUSY_Button', 'image'))
        self.OFFImage = PhotoImage(file=config.get('OFF_Button', 'image'))
        self.SETTINGSImage = PhotoImage(file=config.get('SETTINGS_Button', 'image'))

        self.OK = Button(self)
        self.OK['text'] = config.get('OK_Button', 'text')
        self.OK['fg']   = config.get('OK_Button', 'foreground_colour')
        self.OK['command'] =  lambda: luxafor.fadeRGB(*(config.get('OK_Button', 'colour').split(',')))
        self.OK['image'] = self.OKImg

        self.OK.pack({'side': 'left'})

        self.BUSY = Button(self)
        self.BUSY['text'] = config.get('BUSY_Button', 'text')
        self.BUSY['fg']   = config.get('BUSY_Button', 'foreground_colour')
        self.BUSY['command'] =  lambda: luxafor.fadeRGB(*config.get('BUSY_Button', 'colour').split(','))
        self.BUSY['image'] = self.BUSYImage

        self.BUSY.pack({'side': 'left'})

        self.OFF = Button(self)
        self.OFF['text'] = config.get('OFF_Button', 'text')
        self.OFF['fg']   = config.get('OFF_Button', 'foreground_colour')
        self.OFF['command'] =  lambda: luxafor.fadeRGB(*config.get('OFF_Button', 'colour').split(','))
        self.OFF['image'] = self.OFFImage

        self.OFF.pack({'side': 'left'})

        self.SETTINGS = Button(self)
        self.SETTINGS['text'] = config.get('SETTINGS_Button', 'text')
        self.SETTINGS['fg']   = config.get('SETTINGS_Button', 'foreground_colour')
        self.SETTINGS['command'] =  lambda: self.openSettings()
        self.SETTINGS['image'] = self.SETTINGSImage

        self.SETTINGS.pack({'side': 'left'})

    def setWidget(self, widget, text, fg, command, image):
        if (text != None):
            getattr(self, widget)['text'] = text
        if (fg != None):
            getattr(self, widget)['fg'] = fg
        if (command != None):
            getattr(self, widget)['command'] = command
        if (image != None):
            newImg = PhotoImage(file=image)
            setattr(self, widget + 'Img', newImg)
            getattr(self, widget)['image'] = getattr(self, widget + 'Img')

    def openSettings(self):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', 'settings.cfg'))
        elif os.name == 'nt':
            os.startfile('settings.cfg')
        elif os.name == 'posix':
            subprocess.call(('xdg-open', 'settings.cfg'))

    def createDefaultConfig(self):
        self.config.add_section('OK_Button')
        self.config.set('OK_Button', 'text', 'Ok')
        self.config.set('OK_Button', 'foreground_colour', 'GREEN')
        self.config.set('OK_Button', 'image', 'checkmark.gif')
        self.config.set('OK_Button', 'colour', '0,255,0')
        self.config.set('OK_Button', 'anim', 'fade')

        self.config.add_section('BUSY_Button')
        self.config.set('BUSY_Button', 'text', 'Busy')
        self.config.set('BUSY_Button', 'foreground_colour', 'RED')
        self.config.set('BUSY_Button', 'image', 'cross.gif')
        self.config.set('BUSY_Button', 'colour', '255,0,0')
        self.config.set('BUSY_Button', 'anim', 'fade')

        self.config.add_section('OFF_Button')
        self.config.set('OFF_Button', 'text', 'Off')
        self.config.set('OFF_Button', 'foreground_colour', 'BLACK')
        self.config.set('OFF_Button', 'image', 'switch.gif')
        self.config.set('OFF_Button', 'colour', '0,0,0')
        self.config.set('OFF_Button', 'anim', 'fade')

        self.config.add_section('SETTINGS_Button')
        self.config.set('SETTINGS_Button', 'text', 'Settings')
        self.config.set('SETTINGS_Button', 'foreground_colour', 'BLACK')
        self.config.set('SETTINGS_Button', 'image', 'settings.gif')

        with open('default.cfg', 'wb') as configfile:
            self.config.write(configfile)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.config = ConfigParser.ConfigParser()
        try:
            self.config.readfp(open('default.cfg'))
        except  Exception as e:
            print 'Failed Reading File: ' + str(e)
            self.createDefaultConfig()

        try:
            self.config.readfp(open('settings.cfg'))
        except  Exception as e:
            print 'Failed Reading File: ' + str(e)
            open('settings.cfg', 'a').close()
        self.createWidgets()

# initialise device
try:
    luxafor.initialise()
except  Exception as e:
    print 'Device Could Not Be Initialised: ' + str(e)
else:
    # create root and set to show above other windows
    root = Tk()
    root.title('LuxPanel')
    root.wm_attributes('-topmost', 1)

    # start application
    app = Application(master=root)
    # app.setWidget('OK', None, None, lambda: luxafor.fadeRGB(255,0,0), None) # example of command to change colour
    root.mainloop()

    # turn off luxafor on close
    luxafor.setLuxaforColor(79)