import wikipedia
import re

WORDS = ["WIKIPEDIA","SEARCH","INFORMATION"]

def handle(text,mic,profile):
 

# SEARCH ON WIKIPEDIA	
# STATIC SEARCH

	ny = wikipedia.summary("New York",sentences=3);

	mic.say("%s"% ny)


def isValid(text):

	return bool(re.search(r'\bwikipedia\b',text, re.IGNORECASE))


