# Driver Developer

# How to Use

The Driver Developer takes in a json file as input and writes all necessary setup scripts for a driver to be set up and added to the Driver Registry
The setup scripts are put in the same directory as the json

ex:
	
	python DriverDeveloperPython.py intel.edison.grove.flower.python/DriverRegistryFlowPot.json

	This will populate intel.edison.grove.flower.python with setup scripts to set up a python driver

	
	python DriverDeveloperNode.py intel.edison.grove.flower.node/DriverRegistryFlowPot.json

	This will populate intel.edison.grove.flower.node with setup scripts to set up a node driver

The Driver Developer will create five files each time it is run:

	setup.sh

	GroveSetupRequired.sh

	<kit name>_driver_install.sh

	<kit name>_service_install.sh

	README.md

# Info

The Driver Developer first opens the json file passed to it

All of the json data is then collected in a series of lists

The five files are then written

	# Setup
	
		This is the script that the provisioner will call
		
		It is the main script and calls the other two scripts, GroveSetupRequired.sh and <kit name>_driver_install.sh
		
	# Grove Setup Required
	
		This script installs all necessary dependencies for upm
		
		It downloads and installs mraa
		
		It downloads and installs the parts of upm needed by all drivers
		
	# Driver Install
	
		Installs upm libraries needed for the specific kit driver being created
		
		Calls the DriverWriter with the json file as an argument to create the driver
		
		Calls the service installer
		
	# Service Install
	
		Writes a systemD service that calls the newly created driver on startup
		
		Enables the service to run on startup and immediately starts running it
		
	# README
	
		Gives how to set up the sensors using "type," "name," and "pinNumber" from json
		
		Gives the command to display sensor data using kit name

# JSON Info

All fields are required, at the top level there is "name" and "drivers"

"name" is a string, the value should be the name you want the driver to have ex: flower_pot.py
	
	Make sure to have the name end in .py for python drivers and .js for node drivers

"drivers" is an array of json with the required fields "import," "name," "tag," "units," "type," "pinNumber," "sensorObject," and "dataCollector"

	import
		module to import

	name
		name of the object for this sensor (can be arbitrary)
	
	tag
		the topic published with zeroMQ and the name in the json data sent
	
	units
		units for data sent (used for console print, can be arbitrary)

	type
		the type of sensor it is (Analog, I2C, Digital)

	pinNumber
		number on grove header to plug in to

	sensorObject
		method to call to instantiate the object (use pinNumber where you want the pin number to be placed)
	
	dataCollector
		method to call to collect data from the sensor

	