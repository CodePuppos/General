#
# Welcome to OpenSurf, the open directory finder for Reddit.
# Plap and Jay have designed this program to download directories of cool stuff containing keywords relevant to you.
#

import os
import time
import praw

user_agent = "Keyword Driven Open Directory Downloader by the PupMan and Sidekick Jay"
r = praw.Reddit(user_agent=user_agent)

subreddit = r.get_subreddit('opendirectories')

keyword01 = ''  # enter keyword to search for

list = []

for submission in subreddit.get_hot(limit=5):
    print submission.title
    print submission.url
    if keyword01.lower() in submission.title.lower():  # creates list of all URLs whose post title contains the keyword
        print '\033[1m' + 'FOUND ONE!' + '\033[0m'
        list.append(submission.url)

for submission.url in list:
    print '\033[1m' + '\nGet this one:' + '\033[0m'
    print submission.url

    url = submission.url  # creates a url variable for each relevant URL

    os.chdir('directory to save to')
    os.system('wget -r -np -c --reject "index.html*" --wait=10 %url')  # executes wget to download relevant directory

    time.sleep(300) #waits a while before starting next download



