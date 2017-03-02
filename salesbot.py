import praw
import config
from time import localtime, strftime

sub = "bapcsalescanada"

def bot_login():
    print("Logging in...")
    r = praw.Reddit(#username = config.username,
                    #password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "My BAPCSalesCanada checker!")
    print("Logged in!")
    return r

def run_bot(r):
    fobj = open('output.txt', 'w+')
    myList = []
    count = 1

    print("Obtaining new posts from " + sub)
    for submission in r.subreddit(sub).new(limit=100):
        if "gtx" in submission.title.lower() and ("1080" in submission.title or "1070" in submission.title): 
            myList.append(submission)

    for submission in myList:
        fobj.write(str(count) + ". ")
        fobj.write(submission.title + "\n")
        fobj.write(strftime("%B %d %Y @ %-I:%M %p", localtime(submission.created))+ "\n")
        fobj.write(submission.url + "\n\n")
        count += 1

r = bot_login()
run_bot(r)


