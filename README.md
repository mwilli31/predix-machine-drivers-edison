# predix-machine-drivers-edison
Edison drivers for Predix Machine

# How to Use
The drivers are downloaded and installed from the provision script with the -k argument

	/predix/debian-scripts/provision.sh -k <kit type>

Replace <kit type> with which kit type you would like to download and install, for a full list of kits replace kit type with "help"

View the README for the specific kit you downloaded to learn how to use the sensors and view your data

The README will be placed in:

	/predix/predix-machine-drivers-edison/Install/<kit type>/README.md

# Info
A full list of kits offered is in kits_offered.txt, this file is read to the user when they use the help argument

Each time a new kit is added, the name of the kit's specific directory should be added to kits_offered.txt

If a kit is not on the kits_offered list, the script will stop and provisioning will end

Each kit is placed in its own directory in the Install directory

Each kit contains a setup.sh file, this script should do all necessary calls to download and install dependencies, create the driver and create and start the service

Each kit contains its own README that shows how to set up the kit and how to view your data
