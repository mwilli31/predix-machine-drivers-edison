import json
from pprint import pprint
import sys

#open json file
with open(str(sys.argv[1])) as data_file:
	driverData = json.load(data_file)

print "Reading json"
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

# Name of the kit being made
kitName = str(driverData["name"])[:str(driverData["name"]).rfind('.')]

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
	
print "Writing setup script"
#write setup
setupFile = open(str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "/setup.sh", 'w')

setupFile.write("#!/bin/bash\n"
"./GroveSetupRequired.sh\n"
"./" + kitName + "_driver_install.sh")

setupFile.close()
	
print "Writing Grove Required Setup Script"
#write Grove Setup Required
requiredSetupFile = open(str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "/GroveSetupRequired.sh", 'w')
requiredSetupFile.write("#!/bin/bash\n" +  
"#Download and install mraa\n" +
"echo \"Downloading mraa\"\n" +
"cd /predix/predix-machine-drivers-edison\n" +
"git clone https://github.com/intel-iot-devkit/mraa.git\n" +
"echo \"Installing dependencies\"\n" + 
"apt-get update\n" +
"curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -\n" +
"apt-get install -y --ignore-hold sudo git swig3.0 build-essential python-dev cmake libzmq3-dev nodejs\n" +
"npm install zmq\n" +
"mv /predix/predix-machine-drivers-edison/node_modules/zmq /usr/local/lib/node_modules\n" +
"# Install mraa (complete these steps in the mraa directory)\n" +
"echo \"Installing mraa\"\n" +
"pwd\n" +
"cd mraa\n" +
"mkdir build\n" +
"cd build\n" +
"export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-i386\n" +
"cmake .. -DBUILDSWIGJAVA=ON -DBUILD_SHARED_LIBS=OFF -DJAVA_INCLUDE_PATH=/usr/lib/jvm/java-8-openjdk-i386/include -DJAVA_INCLUDE_PATH2=/usr/lib/jvm/java-8-openjdk-i386/include/linux\n" +
"ln -s /usr/lib/jvm/java-8-openjdk-i386/include/linux/* /usr/lib/jvm/java-8-openjdk-i386/include/\n" +
"make\n" +
"sudo make install\n\n" +
"# Set up upm, this contains drivers for all of your sensors\n" +
"#	clone the directory:\n" +
"cd ..\n" +
"cd ..\n" +
"echo \"Downloading upm\"\n" +
"git clone https://github.com/intel-iot-devkit/upm.git\n\n" +
"# Install upm:\n" +
"echo \"Building UPM\"\n" +
"cd upm\n" +
"pwd\n" +
"mkdir build\n" +
"mv src offered_drivers\n" +
"mkdir src\n" +
"echo \"Copying drivers from offered_drivers to src\"\n" +
"#copy necessary files\n" +
"mv offered_drivers/CMakeLists.txt src\n" +
"mv offered_drivers/pkgconfig.in src\n" +
"mv offered_drivers/package.json.in src\n" +
"mv offered_drivers/javaswig_blacklist src\n" +
"mv offered_drivers/pythonswig_blacklist src\n" +
"mv offered_drivers/nodeswig_blacklist src\n" +
"mv offered_drivers/upm src\n" +
"mv offered_drivers/upm_exception.i src\n" +
"mv offered_drivers/upm.h src\n" +
"mv offered_drivers/upm.i src\n" +
"mv offered_drivers/carrays_float.i src\n" +
"mv offered_drivers/carrays_int16_t.i src\n" +
"mv offered_drivers/carrays_uint16_t.i src\n" +
"mv offered_drivers/carrays_uint32_t.i src\n" +
"mv offered_drivers/carrays_uint8_t.i src\n\n" +
"cd build\n" +
"echo \"Compiling libraries\"\n" +
"cmake .. -DBUILDSWIGJAVA=ON -DBUILD_SHARED_LIBS=OFF -DJAVA_INCLUDE_PATH=/usr/lib/jvm/java-8-openjdk-i386/include -DJAVA_INCLUDE_PATH2=/usr/lib/jvm/java-8-openjdk-i386/include/linux\n" +
"make\n" +
"echo \"Installing libraries\"\n" +
"sudo make install\n\n" +
"echo \"Linking packages\"\n" +
"ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages\n" +
"echo \"Setup Complete\"\n")

requiredSetupFile.close()

print "Writing driver installer"
# Write driver installer
driveInstallFile = open(str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "/" + kitName + "_driver_install.sh", 'w')
driveInstallFile.write("#!/bin/bash\n" + 
"#Find upm\n" +
"cd /predix/predix-machine-drivers-edison/upm\n\n" +
"#Install Drivers\n")

for i in range(0, numDrivers):
	libDirName = importList[i][str(importList[i]).rfind('_') + 1:]
	driveInstallFile.write("mv offered_drivers/" + libDirName + " src\n")
	
driveInstallFile.write("cd build\n" +
"echo \"Compiling libraries\"\n" +
"cmake ..\n" +
"make \n" +
"echo \"Installing libraries\"\n" +
"sudo make install\n\n" +
"echo \"Linking packages\"\n" +
"ln -s /usr/local/lib/python2.7/site-packages/* /usr/local/lib/python2.7/dist-packages\n\n" +
"echo \"Creating drivers\"\n" +
"cd ..\n" +
"cd ..\n" +
"cd Install\n" +
"mv "  + str(driverData["name"]) + " ..\n" +
"cd " + str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "\n" +
"./" + kitName + "_service_install.sh\n")

driveInstallFile.close()

print "Writing Service Installer"
# Write service installer
serviceInstallFile = open(str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "/" + kitName + "_service_install.sh", 'w')

serviceInstallFile.write("#!/bin/bash\n" +
"cd /predix/predix-machine-drivers-edison\n" +
"driverpath=\"$PWD\"\n" +
"#Publish Service\n" +
"echo \'[Unit]\' > /etc/systemd/system/" + kitName + ".service\n" +
"echo \'Description=" + kitName + " Data Publisher\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'After=network.target\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'[Service]\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'ExecStart=/usr/bin/java \'$driverpath\'/" + kitName + "\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'Restart=always\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'RestartSec=10\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'[Install]\' >> /etc/systemd/system/" + kitName + ".service\n" +
"echo \'WantedBy=multi-user.target\' >> /etc/systemd/system/" + kitName + ".service\n" +
"#Start Service\n" +
"sudo systemctl daemon-reload\n" +
"sudo systemctl start " + kitName + "\n" +
"sudo systemctl enable " + kitName + "\n")

serviceInstallFile.close()

print "Writing README"
#write README
readMEFile = open(str(sys.argv[1])[:str(sys.argv[1]).rfind('/')] + "/README.md", 'w')

readMEFile.write("# " + kitName + "\n\n" +
"# Sensor Setup\n")

for i in range(0, numDrivers):
	if typeList[i] == "I2C" :
		readMEFile.write(nameList[i] + " - I2C\n\n")
	else :
		readMEFile.write(nameList[i] + " - " + typeList[i] + " " + pinNumberList[i] + "\n\n")

readMEFile.write("\n# Viewing Data\n" + 
"journalctl -f -u " + kitName)

readMEFile.close()

print "***Complete***"
