#Read from air quality sensor
from time import sleep
import Adafruit_BBIO.ADC as ADC

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
	print level
  sleep(30)
