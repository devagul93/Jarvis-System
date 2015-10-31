# -*- coding: utf-8-*-
import random
import re
import TCPclient as client
from client import jasperpath

WORDS = ["JOKE", "KNOCK KNOCK"]


def getRandomJoke(filename=jasperpath.data('text', 'JOKES.txt')):
    jokeFile = open(filename, "r")
    jokes = []
    start = ""
    end = ""
    for line in jokeFile.readlines():
        line = line.replace("\n", "")

        if start == "":
            start = line
            continue

        if end == "":
            end = line
            continue

        jokes.append((start, end))
        start = ""
        end = ""

    jokes.append((start, end))
    joke = random.choice(jokes)
    return joke


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    joke = getRandomJoke()
    old = "JOKE"

    #mic.say("Knock knock")
    client.send_out("knock knock")

    def firstLine(text):
        #mic.say(joke[0])
	client.send_out(joke[0])
	print "firstLine %s" % text
        def punchLine(text):
            #mic.say(joke[1])
	    client.send_out(joke[1])
	    print "firstLine %s" % text
	old = is_new(text)
        punchLine(old)

    old=is_new(old)
    firstLine(old)


def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bjoke\b', text, re.IGNORECASE))

def is_new(old):
    new = client.grab_input().upper()
    while new==old:
	new = client.grab_input().upper()
    return new
