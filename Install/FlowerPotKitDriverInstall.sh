#Find upm
cd ..
cd upm

#Install Starter Kit Drivers
mv offered_drivers/grove src
mv offered_drivers/guvas12d src
mv offered_drivers/my9221 src
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
python DriverWriter.py DriverRegistryFlowPot.json
mv flowpot_sensor_pub.py ..
./FlowerPotKitServiceInstall.sh
