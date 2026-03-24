#A command line interface to fetch user activity from github, displaying recent activity with time and date
import sys
import json
from urllib import request

def userInput() -> str:
    user_name = sys.argv[1]
    return user_name

def buildURL(user_name) -> str:
    url = f"https://api.github.com/users/{user_name}/events"
    return url

def fetchData(url) -> dict:
    response = request.urlopen(url)
    data = response.read()
    events = json.loads(data)
    return events


def outputData(events):
    print(events[:5])






url = buildURL(userInput())
events = fetchData(url)
outputData(events)



    