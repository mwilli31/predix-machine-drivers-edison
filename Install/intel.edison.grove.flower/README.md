# Flower Pot Kit
# Setup

Plug in sensors as follows

		A0 - Moisture Sensor
		A1 - Light Sensor
		I2C0 (Closest I2C to A0) - Temperature and Humidity Sensor

After plugging in the sensors, reboot the board with the following command
	
		reboot

# Viewing data

To view your data run the following command

		journalctl -f -u flowpot-sensor-pub

# Info
setup calls two scripts, GroveSetupRequired.sh and FlowerPotKitDriverInstall.sh

GroveSetupRequired downloads mraa and upm

mraa is then installed and the libraries necessary for all drivers from upm are installed

FlowerPotKitDriverInstall installs the libraries for the specific sensors in the flower pot kit

	This is done by moving the directories from upm/offered_drivers to upm/src for the specific sensors

	After, the following steps must be followed in upm/build

		cmake .. -DBUILDSWIGNODE=OFF
		make -i
		sudo make install
		ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages

The driver is then written by passing DriverWriter.py the json for the flower pot

The service installer then creates and starts the service for flowpot-sensor-pub