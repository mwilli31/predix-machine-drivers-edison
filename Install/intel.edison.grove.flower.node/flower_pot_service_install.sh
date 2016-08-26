#!/bin/bash
cd /predix/predix-machine-drivers-edison
driverpath="$PWD"
#Publish Service
echo '[Unit]' > /etc/systemd/system/flower_pot.service
echo 'Description=flower_pot Data Publisher' >> /etc/systemd/system/flower_pot.service
echo 'After=network.target' >> /etc/systemd/system/flower_pot.service
echo '' >> /etc/systemd/system/flower_pot.service
echo '[Service]' >> /etc/systemd/system/flower_pot.service
echo 'ExecStart=/usr/bin/node '$driverpath'/flower_pot.js' >> /etc/systemd/system/flower_pot.service
echo 'Restart=always' >> /etc/systemd/system/flower_pot.service
echo 'RestartSec=10' >> /etc/systemd/system/flower_pot.service
echo 'Environment=NODE_ENV=production' >> /etc/systemd/system/flower_pot.service
echo 'Environment=NODE_PATH=/usr/lib/node_modules/:/usr/local/lib/node_modules' >> /etc/systemd/system/flower_pot.service
echo '' >> /etc/systemd/system/flower_pot.service
echo '[Install]' >> /etc/systemd/system/flower_pot.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/flower_pot.service
#Start Service
sudo systemctl daemon-reload
sudo systemctl start flower_pot
sudo systemctl enable flower_pot
