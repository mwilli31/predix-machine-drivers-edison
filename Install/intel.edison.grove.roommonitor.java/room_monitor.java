public class room_monitor { 

	public static void main(String[] args) throws InterruptedException {

		//Create sensor objects
		upm_th02.TH02 temperature = new upm_th02.TH02(6, (short)0x40);
		upm_th02.TH02 humidity = new upm_th02.TH02(6, (short)0x40);
		upm_grove.GroveButton button = new upm_grove.GroveButton(2);
		upm_grove.GroveLight light = new upm_grove.GroveLight(0);
		upm_biss0001.BISS0001 motion = new upm_biss0001.BISS0001(4);
		int quality = 2;
		String jsonString;

		//Create ZeroMQ objects
		//org.zeromq.ZMQ.socket publisher = new org.zeromq.ZMQ.socket(ZMQ.PUB);
		//publisher.bind("tcp://127.0.0.1:35690");

		//Continously collect and publish data from sensors
		while(true) {
	//Publish sensor data
			double temperatureData = temperature.getTemperature();
			//jsonString = "{\"name\": \"Grove_temperatureandhumiditysensor_temperature_1_0-1\", \"datapoints\":[[" + System.currentTimeMillis() + ", " + temperatureData + ", " + quality"]]}";
			//publisher.sendmore("Grove_temperatureandhumiditysensor_temperature_1_0-1");
			//socket.send(org.json.JSONObject(jsonString));
			System.out.println(temperatureData + " degrees Celsius");
			double humidityData = humidity.getHumidity();
			//jsonString = "{\"name\": \"Grove_temperatureandhumiditysensor_humidity_1_0-1\", \"datapoints\":[[" + System.currentTimeMillis() + ", " + humidityData + ", " + quality"]]}";
			//publisher.sendmore("Grove_temperatureandhumiditysensor_humidity_1_0-1");
			//socket.send(org.json.JSONObject(jsonString));
			System.out.println(humidityData + " RH");
			double buttonData = button.value();
			//jsonString = "{\"name\": \"Grove_button_1_1-1\", \"datapoints\":[[" + System.currentTimeMillis() + ", " + buttonData + ", " + quality"]]}";
			//publisher.sendmore("Grove_button_1_1-1");
			//socket.send(org.json.JSONObject(jsonString));
			System.out.println(buttonData + " value for button");
			double lightData = light.raw_value();
			//jsonString = "{\"name\": \"Grove_light_1_1-1\", \"datapoints\":[[" + System.currentTimeMillis() + ", " + lightData + ", " + quality"]]}";
			//publisher.sendmore("Grove_light_1_1-1");
			//socket.send(org.json.JSONObject(jsonString));
			System.out.println(lightData + " raw light value");
			boolean motionData = motion.value();
			//jsonString = "{\"name\": \"Grove_motionsensor_1_4-1\", \"datapoints\":[[" + System.currentTimeMillis() + ", " + motionData + ", " + quality"]]}";
			//publisher.sendmore("Grove_motionsensor_1_4-1");
			//socket.send(org.json.JSONObject(jsonString));
			System.out.println(motionData + " motion boolean");
			System.out.println("-------------------------");

		}
	}
}