if [ -f /etc/udev/rules.d/10-luxafor.rules ]; then
    sudo rm -rf /etc/udev/rules.d/10-luxafor.rules
fi
sudo ./usb-permissions.sh