#!/bin/bash
cd ..
driverpath="$PWD"
cd Install
#Publish Service
echo '[Unit]' > /etc/systemd/system/roommon-sensor-pub.service
echo 'Description=Flower Pot Sensor Data Publisher' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'After=network.target' >> /etc/systemd/system/roommon-sensor-pub.service
echo '' >> /etc/systemd/system/roommon-sensor-pub.service
echo '[Service]' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'ExecStart=/usr/bin/python '$driverpath'/roommon_sensor_pub.py' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'Environment=PYTHONUNBUFFERED=1' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'Restart=always' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'RestartSec=10' >> /etc/systemd/system/roommon-sensor-pub.service
echo '' >> /etc/systemd/system/roommon-sensor-pub.service
echo '[Install]' >> /etc/systemd/system/roommon-sensor-pub.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/roommon-sensor-pub.service
