#!/bin/bash
#Find upm
cd /predix/predix-machine-drivers-edison/upm

#Install Drivers
mv offered_drivers/th02 src
mv offered_drivers/th02 src
mv offered_drivers/grove src
mv offered_drivers/grovemoisture src
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
python DriverWriterNode.py intel.edison.grove.flower.node/DriverRegistryFlowPot.json
mv flower_pot.js ..
cd intel.edison.grove.flower.node
./flower_pot_service_install.sh
