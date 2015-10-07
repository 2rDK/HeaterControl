#!/bin/sh

echo -e "### \e[32mInstalling prerequisites...\e[0m"

apt-get install midori -y
apt-get install python3-pip -y
pip3 install requests
apt-get install libmysqlclient-dev -y
apt-get install python-dev -y
pip3 install mysqlclient

echo -e "### \e[32mSetting up cron...\e[0m"

ThisFolder = pwd

echo -e ThisFolder