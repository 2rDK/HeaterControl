#!/bin/bash

echo -en "### \e[32mInstalling prerequisites...\e[0m\n"

apt-get install midori -y
apt-get install python3-pip -y
pip3 install requests
apt-get install libmysqlclient-dev -y
apt-get install python-dev -y
pip3 install mysqlclient

echo -en "### \e[32mSetting up cron...\e[0m\n"

ThisFolder=$(pwd)

echo $ThisFolder