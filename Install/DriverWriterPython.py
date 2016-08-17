import json
from pprint import pprint
import sys

#open json file
with open(str(sys.argv[1])) as data_file:
	driverData = json.load(data_file)

numDrivers = len(driverData["drivers"])
importList = []
nameList = []
tagList = []
unitsList = []
typeList = []
pinNumberList = []
sensorObjectList = []
dataCollectorList = []

driverFile = open(driverData["name"], 'w')

#collect json data
for i in range(0, numDrivers):
	importList.append(driverData["drivers"][i]["import"])
	nameList.append(driverData["drivers"][i]["name"])
	tagList.append(driverData["drivers"][i]["tag"])
	unitsList.append(driverData["drivers"][i]["units"])
	typeList.append(driverData["drivers"][i]["type"])
	pinNumberList.append(driverData["drivers"][i]["pinNumber"])
	sensorObjectList.append(driverData["drivers"][i]["sensorObject"])
	dataCollectorList.append(driverData["drivers"][i]["dataCollector"])
	
#write imports
driverFile.write("from time import sleep, time\nimport zmq\nfrom json import dumps\nfrom os import getenv\n")
for i in range(0, numDrivers):
	driverFile.write("import " + importList[i] + "\n")
driverFile.write("\n")


#write sensor objects
driverFile.write("#Create sensor objects\n")
for i in range(0, numDrivers):
	sensorString = sensorObjectList[i].replace('pinNumber', pinNumberList[i], 1)
	driverFile.write(nameList[i] + " = " + importList[i] + "." + sensorString + "\n")
driverFile.write("quality = 2\n")

#write zmq objects
driverFile.write("\n#Create ZeroMQ objects\n")
driverFile.write("#Vars from environment\nZMQ_SENSOR_PUB_IP = getenv('ZMQ_SENSOR_PUB_IP', '127.0.0.1')\nZMQ_SENSOR_PUB_PORT = getenv('ZMQ_SENSOR_PUB_PORT', 35690)\nINTERVAL_SEC = int(getenv('INTERVAL_SEC', 3))\ncontext = zmq.Context()\nsocket = context.socket(zmq.PUB)\nsocket.bind(\"tcp://%s:%s\" % (ZMQ_SENSOR_PUB_IP, ZMQ_SENSOR_PUB_PORT))\n\n")

driverFile.write("#Continously collect and publish data from sensors\n")
driverFile.write("while True:\n")

#write data collectors and publishers
driverFile.write("#Publish sensor data\n")
for i in range(0, numDrivers):
		driverFile.write("\t" + nameList[i] + "Data = " + nameList[i] + "." + dataCollectorList[i] + "\n")
		driverFile.write("\tsocket.send_multipart([\'" + tagList[i] + "\', dumps({\"name\": \"" + tagList[i] + "\", \"datapoints\":[[int(time() * 1000), float(" + nameList[i] + "Data), quality]]})])\n")
		driverFile.write("\tprint str(" + nameList[i] + "Data) + \" " + unitsList[i] + "\"\n")

driverFile.write("\tprint \"-------------------------\"\n\n")

driverFile.write("\n\tsleep(INTERVAL_SEC)")
driverFile.close()