import RPi.GPIO as gpio
import re
import TCPclient as client

WORDS = ["SWITCH","ON","LIGHTS"]

def handle(text,mic,profile):
 

# SWITCH light on	
# STATIC SEARCH
	gpio.setmode(gpio.BOARD)
	gpio.setup(12,gpio.OUT)
	gpio.output(12,1)
	ny = "LIGHTS are TURNED ON"
	#mic.say("%s"% ny)
	client.send_out(ny)

def isValid(text):

	return bool(re.search(r'\bon\b',text, re.IGNORECASE))


