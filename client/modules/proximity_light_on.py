import RPi.GPIO as gpio
import time
import re
import TCPclient as client

WORDS = ["MAGIC", "LIGHT"]

def handle(text,mic,profile):

    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    PIR_PIN = 7
    gpio.setup(PIR_PIN, gpio.IN)
    while 1:
        if gpio.input(PIR_PIN):
            print "Motion Detected!"
            gpio.output(12,1)
            time.sleep(10)
            gpio.output(12,0)
	    break
        
def isValid(text):
    return bool(re.search(r'\bmagic\b',text, re.IGNORECASE))
