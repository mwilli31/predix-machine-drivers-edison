#!/bin/bash
cd ..
driverpath="$PWD"
cd Install
#Publish Service
echo '[Unit]' > /etc/systemd/system/flowpot-sensor-pub.service
echo 'Description=Flower Pot Sensor Data Publisher' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'After=network.target' >> /etc/systemd/system/flowpot-sensor-pub.service
echo '' >> /etc/systemd/system/flowpot-sensor-pub.service
echo '[Service]' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'ExecStart=/usr/bin/python '$driverpath'/flowpot_sensor_pub.py' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'Environment=PYTHONUNBUFFERED=1' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'Restart=always' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'RestartSec=10' >> /etc/systemd/system/flowpot-sensor-pub.service
echo '' >> /etc/systemd/system/flowpot-sensor-pub.service
echo '[Install]' >> /etc/systemd/system/flowpot-sensor-pub.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/flowpot-sensor-pub.service
