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

echo -en "\e[32m### Copying staging file to init.d... ###\e[0m\n"
\cp -v $ThisFolder/install/HeaterControlCron /etc/init.d/HeaterControlCron

echo -en "\e[32m### Setting execution permission... ###\e[0m\n"
chmod +x /etc/init.d/HeaterControlCron

echo -en "\e[32m### Adapting to current folder... ###\e[0m\n"
sed -i s/@FOLDER@/'$ThisFolder'/g /etc/init.d/HeaterControlCron

echo -en "\e[32m### Adding to boot sequence... ###\e[0m\n"
update-rc.d HeaterControlCron defaults