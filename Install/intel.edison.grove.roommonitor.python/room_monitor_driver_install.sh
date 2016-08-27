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
cmake .. -DBUILDSWIGNODE=OFF
make -i
echo "Installing libraries"
sudo make install

echo "Linking packages"
ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages

echo "Creating drivers"
cd ..
cd ..
cd Install/intel.edison.grove.roommonitor.python
mv room_monitor.py ../../
echo "Moved drivers"

./room_monitor_service_install.sh
echo "Driver Install Complete"
