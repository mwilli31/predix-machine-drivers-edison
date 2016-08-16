# Driver Writer

# How to Use

The Driver Writer takes in a json file as input and then writes a python driver that publishes grove sensor data to local host port 35690

ex:
	python DriverWriter.py intel.edison.grove.flower/DriverRegistryFlowPot.json

This will output a file flowpot_sensor_pub.py

# Info

The Driver Writer first opens the json file passed to it

It then opens a file to write using the name given in the json

All of the json data is then collected in a series of lists

The Drive writer then begins writing the new driver by writing the required imports

It then creates the data objects for each sensor including the pin number from the json passed

ZeroMQ objects are written which give the ip to publish to, port, and how long the intervals are in between publishing

A while loop is then created that collects the data from the sensors and publishes in json format

# JSON Info

All fields are required, at the top level there is "name" and "drivers"

"name" is a string, the value should be the name you want the driver to have ex: flowpot_sensor_pub.py

"drivers" is an array of json with the required fields "import," "name," "tag," "units," "type," "pinNumber," "sensorObject," "dataCollector," and "publisherId"

	import
		python module to import

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

	