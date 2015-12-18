# LuxaforPanel
Our take on the luxafor control panel. Written in python 2.7

To install you will need:  
python-tk  
pyusb

## Dependency Installation
1. Install the pyusb libraries (currently requires --pre flag)
    ```
    apt-get install python-pip
    pip install --pre pyusb
    ```
2. Install tk-inter for python
    ```
    apt-get install python-tk
    ```

3. Run the permissions fix to add the Luxafor usb device to udev rules list
    ```
    ./usb-permissions.sh
    ```
  
## Enjoy!

Icons created by [Keyamoon](http://keyamoon.com/) used under the [CC-BY 4.0](http://creativecommons.org/licenses/by/4.0/) license. Icons were converted into an alternative format for use in this project.
