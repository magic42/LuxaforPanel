if [ ! -f /etc/udev/rules.d/10-luxafor.rules ]; then
    sudo touch /etc/udev/rules.d/10-luxafor.rules
    sudo echo "SUBSYSTEM==\"usb\", ATTRS{idProduct}==\"f372\", ATTRS{idVendor}==\"04d8\", MODE=\"666\"" >> /etc/udev/rules.d/10-luxafor.rules
fi