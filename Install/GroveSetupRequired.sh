#Download and install mraa
echo "Downloading mraa"
cd ..
git clone https://github.com/intel-iot-devkit/mraa.git
echo "Installing dependencies"
apt-get update
apt-get --ignore-hold install sudo
apt-get update
sudo apt-get install -y --ignore-hold git build-essential swig3.0 python-dev nodejs-dev cmake libzmq3-dev python-zmq

# Install mraa (complete these steps in the mraa directory)
echo "Installing mraa"	
pwd
cd mraa	
mkdir build
cd build
cmake .. -DBUILDSWIGNODE=OFF
make
sudo make install

# Set up upm, this contains drivers for all of your sensors
#	clone the directory:
cd ..
cd ..
echo "Downloading upm"
git clone https://github.com/intel-iot-devkit/upm.git

# Install upm:
echo "Building UPM"
cd upm
pwd
mkdir build
mv src offered_drivers
mkdir src
echo "Copying drivers from offered_drivers to src"
#copy necessary files
mv offered_drivers/CMakeLists.txt src
mv offered_drivers/pkgconfig.in src
mv offered_drivers/javaswig_blacklist src
mv offered_drivers/pythonswig_blacklist src
mv offered_drivers/nodeswig_blacklist src
mv offered_drivers/upm src
mv offered_drivers/upm_exception.i src
mv offered_drivers/upm.h src
mv offered_drivers/upm.i src
mv offered_drivers/carrays_float.i src
mv offered_drivers/carrays_int16_t.i src
mv offered_drivers/carrays_uint16_t.i src
mv offered_drivers/carrays_uint32_t.i src
mv offered_drivers/carrays_uint8_t.i src

cd build
echo "Compiling libraries"
cmake .. -DBUILDSWIGNODE=OFF
make -i
echo "Installing libraries"
sudo make install

echo "Linking packages"
ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages
echo "Setup Complete"
cd ../../Install
