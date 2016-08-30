from time import sleep, time
import zmq
from json import dumps
from os import getenv
import pyupm_th02
import pyupm_th02
import pyupm_grove
import pyupm_grove
import pyupm_biss0001

#Create sensor objects
temperature = pyupm_th02.TH02(3, 0x40)
humidity = pyupm_th02.TH02(3, 0x40)
button = pyupm_grove.GroveButton(2)
light = pyupm_grove.GroveLight(0)
motion = pyupm_biss0001.BISS0001(4)
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
	socket.send_multipart(['temperature', dumps({"name": "temperature_1", "datapoints":[[int(time() * 1000), float(temperatureData), quality]]})])
	print str(temperatureData) + " degrees Celsius"
	humidityData = humidity.getHumidity()
	socket.send_multipart(['humidity', dumps({"name": "humidity_1", "datapoints":[[int(time() * 1000), float(humidityData), quality]]})])
	print str(humidityData) + " RH"
	buttonData = button.value()
	socket.send_multipart(['button', dumps({"name": "button_1", "datapoints":[[int(time() * 1000), float(buttonData), quality]]})])
	print str(buttonData) + " value for button"
	lightData = light.raw_value()
	socket.send_multipart(['light', dumps({"name": "light_1", "datapoints":[[int(time() * 1000), float(lightData), quality]]})])
	print str(lightData) + " raw light value"
	motionData = motion.value()
	socket.send_multipart(['motion', dumps({"name": "motion_1", "datapoints":[[int(time() * 1000), float(motionData), quality]]})])
	print str(motionData) + " motion boolean"
	print "-------------------------"


	sleep(INTERVAL_SEC)
