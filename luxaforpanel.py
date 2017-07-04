#!/usr/bin/env python
import luxafor
import time, subprocess, os
import ConfigParser
from Tkinter import *
import dbus

class Application(Frame):
    sys_bus = dbus.SystemBus()

    def createWidget(self, name):
        config = self.config

        setattr(self, name + '_IMG', False)        

        if (config.has_option(name, 'image')) : 
            if (config.get(name, 'image') != 'none') :
                setattr(self, name + '_IMG', PhotoImage(file=config.get(name, 'image')))

        setattr(self, name, Button(self))
        getattr(self, name)['text'] = config.get(name, 'text')
        getattr(self, name)['fg']   = config.get(name, 'foreground_colour')
        getattr(self, name)['command'] =  lambda: luxafor.fadeRGB(*(config.get(name, 'colour').split(',')))
        if (getattr(self, name + '_IMG')) :
            getattr(self, name)['image'] = getattr(self, name + '_IMG')

        if (config.has_option(name, 'align')) : 
            getattr(self, name).pack({'side': config.get(name, 'align')})
        else:
            getattr(self, name).pack({'side': 'left'})

    def createWidgets(self):
        config = self.config

        for section in config.sections():
            self.createWidget(section)

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

        with open('default.cfg', 'wb') as configfile:
            self.config.write(configfile)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.config = ConfigParser.ConfigParser()

        self.config.add_section('OFF_Button')
        self.config.set('OFF_Button', 'text', 'Off')
        self.config.set('OFF_Button', 'foreground_colour', 'BLACK')
        self.config.set('OFF_Button', 'image', 'switch.gif')
        self.config.set('OFF_Button', 'colour', '0,0,0')
        self.config.set('OFF_Button', 'anim', 'fade')
        self.config.set('OFF_Button', 'align', 'right')

        self.config.add_section('SETTINGS_Button')
        self.config.set('SETTINGS_Button', 'text', 'Settings')
        self.config.set('SETTINGS_Button', 'foreground_colour', 'BLACK')
        self.config.set('SETTINGS_Button', 'image', 'settings.gif')
        self.config.set('SETTINGS_Button', 'align', 'right')

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