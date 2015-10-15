#!/bin/bash

echo -en "\e[32m### Installing prerequisites... ###\e[0m\n"

apt-get install midori -y
apt-get install python3-pip -y
pip3 install requests
apt-get install libmysqlclient-dev -y
apt-get install python-dev -y
pip3 install mysqlclient
pip3 install tornado

echo -en "\e[32m### Setting up cron... ###\e[0m\n"

ThisFolder=$(pwd)

echo $ThisFolder

echo -en "\e[32m### Copying staging files to init.d... ###\e[0m\n"
\cp -v $ThisFolder/install/HeaterControlFront /etc/init.d/HeaterControlFront
\cp -v $ThisFolder/install/HeaterControlBack /etc/init.d/HeaterControlBack

echo -en "\e[32m### Setting execution permissions... ###\e[0m\n"
chmod +x /etc/init.d/HeaterControlFront
chmod +x /etc/init.d/HeaterControlBack

echo -en "\e[32m### Adapting to current folder... ###\e[0m\n"
sed -i -e "s|@FOLDER@|$ThisFolder|g" /etc/init.d/HeaterControlFront
sed -i -e "s|@FOLDER@|$ThisFolder|g" /etc/init.d/HeaterControlBack
echo -en "\e[32m### Adding to boot sequence... ###\e[0m\n"
update-rc.d HeaterControlFront defaults
update-rc.d HeaterControlBack defaults