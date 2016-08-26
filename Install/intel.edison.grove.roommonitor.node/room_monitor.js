var zmq = require('zmq');
var jsupm_th02 = require('jsupm_th02');
var jsupm_th02 = require('jsupm_th02');
var jsupm_grove = require('jsupm_grove');
var jsupm_grove = require('jsupm_grove');
var jsupm_biss0001 = require('jsupm_biss0001');

//Create sensor objects
var temperature = new jsupm_th02.TH02(3, 0x40);
var humidity = new jsupm_th02.TH02(3, 0x40);
var button = new jsupm_grove.GroveButton(2);
var light = new jsupm_grove.GroveLight(0);
var motion = new jsupm_biss0001.BISS0001(4);
var quality = 2;

//Create ZeroMQ objects
var socket = zmq.socket('pub');
socket.bind('tcp://127.0.0.1:35690');

//Create data object
var timeMS = new Date();

//Continously collect and publish data from sensors
function sensorPub() {
	//Publish sensor data
	temperatureData = temperature.getTemperature();
	socket.send(['Grove_temperatureandhumiditysensor_temperature_1_0-1', JSON.stringify({"name": "Grove_temperatureandhumiditysensor_temperature_1_0-1", "datapoints":[[timeMS.getTime(), temperatureData, quality]]})]);
	console.log(temperatureData + " degrees Celsius");
	humidityData = humidity.getHumidity();
	socket.send(['Grove_temperatureandhumiditysensor_humidity_1_0-1', JSON.stringify({"name": "Grove_temperatureandhumiditysensor_humidity_1_0-1", "datapoints":[[timeMS.getTime(), humidityData, quality]]})]);
	console.log(humidityData + " RH");
	buttonData = button.value();
	socket.send(['Grove_button_1_1-1', JSON.stringify({"name": "Grove_button_1_1-1", "datapoints":[[timeMS.getTime(), buttonData, quality]]})]);
	console.log(buttonData + " value for button");
	lightData = light.raw_value();
	socket.send(['Grove_light_1_1-1', JSON.stringify({"name": "Grove_light_1_1-1", "datapoints":[[timeMS.getTime(), lightData, quality]]})]);
	console.log(lightData + " raw light value");
	motionData = motion.value();
	socket.send(['Grove_motionsensor_1_4-1', JSON.stringify({"name": "Grove_motionsensor_1_4-1", "datapoints":[[timeMS.getTime(), motionData, quality]]})]);
	console.log(motionData + " motion boolean");
	console.log("-------------------------");

}
	setInterval(sensorPub, 3000);