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
publisherIdList = []

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
	publisherIdList.append(driverData["drivers"][i]["publisherId"])
	
#write imports
driverFile.write("var zmq = require('zmq');\n")
for i in range(0, numDrivers):
	driverFile.write("var " + importList[i] + " = require(\'" + importList[i] + "\');\n")
driverFile.write("\n")


#write sensor objects
driverFile.write("//Create sensor objects\n")
for i in range(0, numDrivers):
	sensorString = sensorObjectList[i].replace('pinNumber', pinNumberList[i], 1)
	driverFile.write("var " + nameList[i] + " = new " + importList[i] + "." + sensorString + ";\n")
driverFile.write("var quality = 2;\n")

#write zmq objects
driverFile.write("\n//Create ZeroMQ objects\n")
driverFile.write("var socket = zmq.socket(\'pub\');\nsocket.bind(\'tcp://127.0.0.1:35690\');\n\n//Create data object\nvar timeMS = new Date();\n\n")

driverFile.write("//Continously collect and publish data from sensors\n")
driverFile.write("function sensorPub() {\n")

#write data collectors and publishers
driverFile.write("\t//Publish sensor data\n")
for i in range(0, numDrivers):
		driverFile.write("\t" + nameList[i] + "Data = " + nameList[i] + "." + dataCollectorList[i] + ";\n")
		driverFile.write("\tsocket.send([\'" + tagList[i] + "\', JSON.stringify({\"name\": \"" + tagList[i] + "\", \"datapoints\":[[timeMS.getTime(), " + nameList[i] + "Data, quality]]})]);\n")
		driverFile.write("\tconsole.log(" + nameList[i] + "Data + \" " + unitsList[i] + "\");\n")

driverFile.write("\tconsole.log(\"-------------------------\");\n\n")

driverFile.write("}\n\tsetInterval(sensorPub, 3000);")
driverFile.close()
