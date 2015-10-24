# HeaterControl
Using a Raspberry Pi to control an electric radiator
## Install instructions

###Make RPi boot into kiosk mode
Enable boot to desktop:
```
sudo raspi-config
```
Install chromium:
```
sudo apt-get install chromium
```
Start chromium when RPi boots
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
Add the following line:
```
@chromium --kiosk --ignore-certificate-errors --disable-restore-session-state "http://localhost:8888"
```

###Display driver
Download LCD-show-150602.tar.gz from http://www.waveshare.com/wiki/5inch_HDMI_LCD

Run
```
sudo ./LCD5-show
```
This will induce kernel panic, but do not panic :)
Reboot and hold Shift for NOOBS recovery mode.
press e, change cmdline.txt from:
```
root=/dev/mmcblk0p2
```
to:
```
root=/dev/mmcblk0p6
```
Close the NOOBS interface and power off the pi. Connect the 5" LCD and repower.
