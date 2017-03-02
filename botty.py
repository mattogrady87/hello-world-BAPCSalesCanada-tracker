import praw
import config
from time import localtime, strftime
import os

sub = "bapcsalescanada"

def bot_login():
    print("Logging in...")
    r = praw.Reddit(client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "My BAPCSalesCanada checker!")
    print("Logged in!")
    return r

def outputChk(mode='r'):

    try:
        with open('output.txt', 'r') as f: origOutput = f.read()
        return origOutput

    except FileNotFoundError:
        print("No output.txt file found, creating now...")
        with open('output.txt', 'a'):
            os.utime('output.txt', None)
        with open('output.txt', 'r') as f: origOutput = f.read()
        return origOutput

def run_bot(r):
    #get the previous data inside output.txt if it exists
    origOutput = outputChk()
    newItemList = []

    print("Obtaining new posts from " + sub)

    for submission in r.subreddit(sub).new(limit=100):
        if "gtx" in submission.title.lower() and ("1080" in submission.title or "1070" in submission.title) and submission.title not in origOutput:

            print("Got one")
            newItemList.append(submission)

    if newItemList:
        modOutput = open('output.txt', 'w+')
        for submission in newItemList:
            modOutput.write(submission.title + "\n")
            modOutput.write(strftime("%B %d %Y @ %-I:%M %p", localtime(submission.created)) + "\n")
            modOutput.write(submission.url + "\n\n")
        modOutput.write(origOutput)



r = bot_login()
run_bot(r)
