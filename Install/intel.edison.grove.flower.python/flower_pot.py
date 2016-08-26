from time import sleep, time
import zmq
from json import dumps
from os import getenv
import pyupm_th02
import pyupm_th02
import pyupm_grove
import pyupm_grovemoisture

#Create sensor objects
temperature = pyupm_th02.TH02(3, 0x40)
humidity = pyupm_th02.TH02(3, 0x40)
light = pyupm_grove.GroveLight(1)
moisture = pyupm_grovemoisture.GroveMoisture(0)
quality = 2

#Create ZeroMQ objects
#Vars from environment
ZMQ_SENSOR_PUB_IP = getenv('ZMQ_SENSOR_PUB_IP', '127.0.0.1')
ZMQ_SENSOR_PUB_PORT = getenv('ZMQ_SENSOR_PUB_PORT', 35690)
INTERVAL_SEC = int(getenv('INTERVAL_SEC', 3))
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://%s:%s" % (ZMQ_SENSOR_PUB_IP, ZMQ_SENSOR_PUB_PORT))

#Continously collect and publish data from sensors
while True:
#Publish sensor data
	temperatureData = temperature.getTemperature()
	socket.send_multipart(['Grove_temperatureandhumiditysensor_temperature_1_0-1', dumps({"name": "Grove_temperatureandhumiditysensor_temperature_1_0-1", "datapoints":[[int(time() * 1000), float(temperatureData), quality]]})])
	print str(temperatureData) + " degrees Celsius"
	humidityData = humidity.getHumidity()
	socket.send_multipart(['Grove_temperatureandhumiditysensor_humidity_1_0-1', dumps({"name": "Grove_temperatureandhumiditysensor_humidity_1_0-1", "datapoints":[[int(time() * 1000), float(humidityData), quality]]})])
	print str(humidityData) + " RH"
	lightData = light.raw_value()
	socket.send_multipart(['Grove_light_1_1-1', dumps({"name": "Grove_light_1_1-1", "datapoints":[[int(time() * 1000), float(lightData), quality]]})])
	print str(lightData) + " raw light value"
	moistureData = moisture.value()
	socket.send_multipart(['Grove_moisturesensor_1_4-1', dumps({"name": "Grove_moisturesensor_1_4-1", "datapoints":[[int(time() * 1000), float(moistureData), quality]]})])
	print str(moistureData) + " moisture value"
	print "-------------------------"


	sleep(INTERVAL_SEC)