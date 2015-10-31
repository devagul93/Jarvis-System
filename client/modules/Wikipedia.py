import wikipedia
import re
import TCPclient as client

WORDS = ["WIKIPEDIA","SEARCH","INFORMATION"]

def handle(text,mic,profile):
 

# SEARCH ON WIKIPEDIA	
#	ny = wikipedia.summary("New York",sentences=3);
#	mic.say("%s"% ny)
	
	#mic.say("What you want to search about")
	#text = mic.activeListen()
	print "entering wiki term"
        text = client.grab_input()
	while text.upper()=="WIKIPEDIA":
            print "entering while"
	    text = client.grab_input()
	    print text

	answer = wikipedia.summary(text,sentences=3)
	answer +="\n" 
	print answer
	client.send_out(answer)

	#mic.say(answer)


def isValid(text):

	return bool(re.search(r'\bwikipedia\b',text, re.IGNORECASE))


