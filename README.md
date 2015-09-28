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
