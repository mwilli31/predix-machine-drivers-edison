#!/bin/bash
#Find upm
cd /predix/predix-machine-drivers-edison/upm

#Install Starter Kit Drivers
mv offered_drivers/grove src
mv offered_drivers/guvas12d src
mv offered_drivers/th02 src
mv offered_drivers/biss0001 src
cd build
echo "Compiling libraries"
cmake .. -DBUILDSWIGNODE=OFF
make -i
echo "Installing libraries"
sudo make install

echo "Linking packages"
ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages

echo "Creating drivers"
cd /predix/predix-machine-drivers-edison/Install
python DriverWriter.py intel.edison.grove.roommonitor/DriverRegistryRoomMon.json
mv roommon_sensor_pub.py ..
cd intel.edison.grove.roommonitor
./RoomMonKitServiceInstall.sh
