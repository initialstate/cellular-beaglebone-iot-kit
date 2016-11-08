#Read from air quality sensor
from time import sleep
import Adafruit_BBIO.ADC as ADC
from ISStreamer.Streamer import Streamer

#Initialize the streamer
streamer = Streamer(bucket_name="BBB Readings", bucket_key="bbbreadings", access_key="[Place Your Access Key Here]")

pin = "AIN0"

ADC.setup()

while True:
	value=ADC.read_raw(pin)
	if value > 700:
        	level="High pollution"
        elif value > 300:
        	level="Low pollution"
        else:
        	level="Air fresh"
        print value
        #Stream the value
        streamer.log(":cloud:Sensor Reading",value)
        print level
        #Stream the level
        streamer.log(":wind_blowing_face:Air Quality",level)
        #Sleep for 1 minute
        sleep(60)
