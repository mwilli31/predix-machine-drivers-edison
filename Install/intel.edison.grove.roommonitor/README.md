# Room Monitor Kit
# Setup

Plug in sensors as follows

		A0 - Light Sensor
		D2 - Button
		D4 - Motion Sensor
		I2C0 (Closest I2C to A0) - Temperature and Humidity Sensor

After plugging in the sensors, reboot the board with the following command
	
		reboot

# Viewing data

To view your data run the following command

		journalctl -f -u roommon-sensor-pub