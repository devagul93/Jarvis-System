import RPi.GPIO as gpio
import re
import TCPclient as client

WORDS = ["TURN", "OFF","LIGHT"]

def handle(text,mic,profile):
 

# SWITCH light on	
# STATIC SEARCH
	gpio.setmode(gpio.BOARD)
	gpio.setup(12,gpio.OUT)
	gpio.output(12,0)
	ny = "LIGHTS are TURNED OFF"
	#mic.say("%s"% ny)
	client.send_out(ny)

def isValid(text):

	return bool(re.search(r'\boff\b',text, re.IGNORECASE))


