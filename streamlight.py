#Read from light sensor
from time import sleep
import Adafruit_BBIO.ADC as ADC
from ISStreamer.Streamer import Streamer

#Initialize the streamer
streamer = Streamer(bucket_name="BBB Readings", bucket_key="bbbreadings", access_key="[Place Your Access Key Here]")

pin = "AIN2"

ADC.setup()

while True:
	value=ADC.read_raw(pin)
	if value<=250:
		level="dim"
	if 251<=value<=500:
		level="average"
	if 501<=value<=800:
		level="bright"
	if value>800:
		level="very bright"
  	print value
  	#Stream the value
  	streamer.log(":level_slider:Sensor Reading",value)
	print level
	#Stream the level
  	streamer.log(":bulb:Brightness",level)
  	#Sleep for 1 minute
   	sleep(60)
