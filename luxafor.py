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

# find device and detatch device driver
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
    dev.write(1, [0, color])

# rgb colour
def setRGB(r, g, b, led = 255): # led can be used to specify an led in the device numbered 1-6 to be individually lit, led 255 lights all leds
    dev.write(1, [1, led, r, g, b])

# fade in rgb
def fadeRGB(r, g, b, duration = 50, led = 255):
    dev.write(1, [2, led, r, g, b, duration])

# flashing rgb
def flashRGB(r, g, b, duration = 10, repeat = 5, led = 255): # note that upon completion of the flashing sequence the colour of led 1 is applied to led 255 changing the whole array to the same colour
    dev.write(1, [3, led, r, g, b, duration, 0, repeat])