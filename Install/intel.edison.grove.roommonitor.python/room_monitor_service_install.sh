#!/bin/bash
cd /predix/predix-machine-drivers-edison
driverpath="$PWD"
#Publish Service
echo '[Unit]' > /etc/systemd/system/room_monitor.service
echo 'Description=room_monitor Data Publisher' >> /etc/systemd/system/room_monitor.service
echo 'After=network.target' >> /etc/systemd/system/room_monitor.service
echo '' >> /etc/systemd/system/room_monitor.service
echo '[Service]' >> /etc/systemd/system/room_monitor.service
echo 'ExecStart=/usr/bin/python '$driverpath'/room_monitor.py' >> /etc/systemd/system/room_monitor.service
echo 'Environment=PYTHONUNBUFFERED=1' >> /etc/systemd/system/room_monitor.service
echo 'Restart=always' >> /etc/systemd/system/room_monitor.service
echo 'RestartSec=10' >> /etc/systemd/system/room_monitor.service
echo '' >> /etc/systemd/system/room_monitor.service
echo '[Install]' >> /etc/systemd/system/room_monitor.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/room_monitor.service
#Start Service
sudo systemctl daemon-reload
sudo systemctl start room_monitor
sudo systemctl enable room_monitor
