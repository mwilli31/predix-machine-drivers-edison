#!/bin/bash
cd /predix/predix-machine-drivers-edison
driverpath="$PWD"
#Publish Service
echo '[Unit]' > /etc/systemd/system/room_monitor.service
echo 'Description=room_monitor Data Publisher' >> /etc/systemd/system/room_monitor.service
echo 'After=network.target' >> /etc/systemd/system/room_monitor.service
echo '' >> /etc/systemd/system/room_monitor.service
echo '[Service]' >> /etc/systemd/system/room_monitor.service
echo 'ExecStart=/usr/bin/node '$driverpath'/room_monitor.js' >> /etc/systemd/system/room_monitor.service
echo 'Restart=always' >> /etc/systemd/system/room_monitor.service
echo 'RestartSec=10' >> /etc/systemd/system/room_monitor.service
echo 'Environment=NODE_ENV=production' >> /etc/systemd/system/room_monitor.service
echo 'Environment=NODE_PATH=/usr/lib/node_modules/:/usr/local/lib/node_modules' >> /etc/systemd/system/room_monitor.service
echo '' >> /etc/systemd/system/room_monitor.service
echo '[Install]' >> /etc/systemd/system/room_monitor.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/room_monitor.service
#Start Service
sudo systemctl daemon-reload
sudo systemctl start room_monitor
sudo systemctl enable room_monitor
