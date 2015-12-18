import usb.core
import usb.util
import sys

luxCols = {
    "blue"    : 66,
    "cyan"    : 67,
    "green"   : 71,
    "magenta" : 77,
    "off"     : 79,
    "red"     : 82,
    "white"   : 87,
    "yellow"  : 89
}

dev = None

def initialise():
    # find device and detatch device driver
    global dev
    dev = usb.core.find(idVendor=0x04d8, idProduct=0xf372)

    if dev is None:
        raise ValueError('Device not found')

    try:
        dev.detach_kernel_driver(0)
    except Exception, e:
        pass
     
     # initial configuration
    dev.set_configuration()

# luxafor colour (see luxCols for codes)
def setLuxaforColor(color):
    if color in luxCols:
        color = luxCols[color]
    write([0, color])

# rgb colour
def setRGB(r, g, b):
    write([1, 255, r, g, b])

# fade in rgb
def fadeRGB(r, g, b, duration = 50):
    write([2, 255, r, g, b, duration])

# flashing rgb
def flashRGB(r, g, b, duration = 10, repeat = 5):
    write([3, 255, r, g, b, duration, 0, repeat])

# write to device
def write(input):
    try:
        dev.write(1, input);
    except Exception, e:
        initialise()
        dev.write(1, input);
        pass