#Read from light sensor
from time import sleep
import Adafruit_BBIO.ADC as ADC

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
  sleep(30)
