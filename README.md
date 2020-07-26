# nfc-test

run follow command in host-machine
```bash
sudo modprobe -r port100
sudo sh -c 'echo blacklist port100 >> /etc/modprobe.d/blacklist-nfc.conf'
sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
sudo udevadm control -R
```
