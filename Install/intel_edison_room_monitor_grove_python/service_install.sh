#!/bin/bash
cd /predix/predix-machine-drivers-edison
driverpath="$PWD"
#Publish Service
echo '[Unit]' > /etc/systemd/system/driver.service
echo 'Description=room_monitor Data Publisher' >> /etc/systemd/system/driver.service
echo 'After=network.target' >> /etc/systemd/system/driver.service
echo '' >> /etc/systemd/system/driver.service
echo '[Service]' >> /etc/systemd/system/driver.service
echo 'ExecStart=/usr/bin/python '$driverpath'/room_monitor.py' >> /etc/systemd/system/driver.service
echo 'Environment=PYTHONUNBUFFERED=1' >> /etc/systemd/system/driver.service
echo 'Restart=always' >> /etc/systemd/system/driver.service
echo 'RestartSec=10' >> /etc/systemd/system/driver.service
echo '' >> /etc/systemd/system/driver.service
echo '[Install]' >> /etc/systemd/system/driver.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/driver.service
#Start Service
sudo systemctl daemon-reload
sudo systemctl start driver
sudo systemctl enable driver
