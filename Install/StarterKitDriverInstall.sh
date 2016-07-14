#Find upm
cd ..
driverpath="$PWD"
cd upm

#Install Starter Kit Drivers
mv offered_drivers/grove src
mv offered_drivers/rotaryencoder src
mv offered_drivers/gas src
mv offered_drivers/th02 src
mv offered_drivers/guvas12d src
mv offered_drivers/my9221 src
mv offered_drivers/lcd src
cd build
echo "Compiling libraries"
cmake .. -DBUILDSWIGNODE=OFF
make -i
echo "Installing libraries"
sudo make install

echo "Linking packages"
ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages

echo "Creating drivers"
cd .. 
cd ..
cd Install
python DriverWriter.py
mv starter_sensor_pub.py ..

#Publish Service
echo '[Unit]' > /etc/systemd/system/starter-sensor-pub.service
echo 'Description=Grove Sensor Data Publisher' >> /etc/systemd/system/starter-sensor-pub.service
echo 'After=network.target' >> /etc/systemd/system/starter-sensor-pub.service
echo '' >> /etc/systemd/system/starter-sensor-pub.service
echo '[Service]' >> /etc/systemd/system/starter-sensor-pub.service
echo 'ExecStart=/usr/bin/python '$driverpath'/starter_sensor_pub.py' >> /etc/systemd/system/starter-sensor-pub.service
echo 'Environment=PYTHONUNBUFFERED=1' >> /etc/systemd/system/starter-sensor-pub.service
echo 'Restart=always' >> /etc/systemd/system/starter-sensor-pub.service
echo 'RestartSec=10' >> /etc/systemd/system/starter-sensor-pub.service
echo '' >> /etc/systemd/system/starter-sensor-pub.service
echo '[Install]' >> /etc/systemd/system/starter-sensor-pub.service
echo 'WantedBy=multi-user.target' >> /etc/systemd/system/starter-sensor-pub.service

