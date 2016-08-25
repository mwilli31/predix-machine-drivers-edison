#!/bin/bash
#Find upm
cd /predix/predix-machine-drivers-edison/upm

#Install Drivers
mv offered_drivers/th02 src
mv offered_drivers/th02 src
mv offered_drivers/grove src
mv offered_drivers/grove src
mv offered_drivers/biss0001 src
cd build
echo "Compiling libraries"
cmake ..
make 
echo "Installing libraries"
sudo make install

echo "Linking packages"
ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages

echo "Creating drivers"
cd ..
cd ..
cd Install
mv room_monitor.java ..
cd intel.edison.grove.roommonitor.java
./room_monitor_service_install.sh
