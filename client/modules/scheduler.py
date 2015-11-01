import wikipedia
import re
import TCPclient as client

WORDS = ["scheduler"]

def handle(text,mic,profile):
 

# SEARCH ON WIKIPEDIA	
#	ny = wikipedia.summary("New York",sentences=3);
#	mic.say("%s"% ny)
	
	#mic.say("")
	#text = mic.activeListen()
	list = "8 AM   go to college "
	client.send_out("ADD or LISTEN")
        text = client.grab_input()
	while text.upper()=="SCHEDULER":
	    text = client.grab_input()
	if text.upper()=="ADD":
	    while text.upper()=="ADD":
                text = client.grab_input()
	    list += text + "              "
	    client.send_out("added to list, your schedule for today is " + list)
	    client.send_out(list)
	else:
	    client.send_out("Your schedule for today is ")
	    client.send_out(list)


	#mic.say(answer)


def isValid(text):

	return bool(re.search(r'\bscheduler\b',text, re.IGNORECASE))


