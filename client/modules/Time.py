# -*- coding: utf-8-*-
import datetime
import re
import TCPclient as tcp

from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["TIME"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    service = DateService()
    response = service.convertTime(now)
    #mic.say("It is %s right now." % response)
    timeNow =  "It is "+response+" right now"
    tcp.send_out(timeNow)

def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btime\b', text, re.IGNORECASE))
