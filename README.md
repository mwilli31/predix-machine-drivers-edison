# predix-machine-drivers-edison
Edison drivers for Predix Machine

# Setting up mraa and upm
Mraa and upm are required by all grove sensors to be able to interact with the Edison.
To install mraa and upm:
	
	cd /predix/predix-machine-drivers-edison/Install
	./GroveSetupRequired.sh

This command will install the required dependencies for mraa and upm, clone both from github, and install necessary libraries.
However, this script is called by /predix/InitialSetup.sh and is included already in the flash image.

# Setting up the Starter Kit Sensors
To install the specific sensors for the Starter Kit:
	
	cd /predix
	./provision.sh

This script will update all files from git. 
Also, it will call StarterKitDriverInstall.sh. This will install the necessary libraries from upm for the specific sensors and call DriverWriter.py.
DriverWriter will write a python driver to collect and publish data using ZeroMQ according to the data in DriverRegistryStarter.json.
Following the creation of the driver, StarterKitDriverInstall.sh will create a SystemD service to start running the new driver in the background on startup.
By default the data will publish to tcp://127.0.0.1:35690, local host. Flowthings will then take this data and upload it to flowthings.

# Collecting and Publishing data
Since the SystemD service is already created and running, the only necessary step is to attach the Grove Header to the board and attach the sensors. After attaching the sensors, restart the board.
The default placement of the sensors are: 
	
	A2 - Grove Light Sensor
	A3 - Grove UV Sensor
	UART - Grove Button
	D2 - Grove Encoder
	12C1 - Grove Temperature & Humidity Sensor

# Viewing the data
After attaching the sensors and restarting the board, run the following command to view the data.

	journalctl -f -u starter-sensor-pub
