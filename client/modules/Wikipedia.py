import wikipedia
import re

WORDS = ["WIKIPEDIA","SEARCH","INFORMATION"]

def handle(text,mic,profile):
 

# SEARCH ON WIKIPEDIA	
#	ny = wikipedia.summary("New York",sentences=3);
#	mic.say("%s"% ny)

	mic.say("What you want to search about")
	text = mic.activeListen()

	answer = wikipedia.summary(text,sentences=3)

	mic.say(answer)


def isValid(text):

	return bool(re.search(r'\bwikipedia\b',text, re.IGNORECASE))


