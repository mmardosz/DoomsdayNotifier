# M. MARDOSZ
#
# Using Python 2.7
#
# Dependencies:
# - python-twitter
# - pygame
# - gTTS

import twitter
import time
# from requests.exceptions import ConnectionError
import pygame
from time import sleep
from gtts import gTTS
import os
import re

# twitter ID instead of username
TWITTER_ID = 25073877
CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_TOKEN = 'x'
ACCESS_TOKEN_SECRET = 'x'
QUEUE_SIZE = 5


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class DoomsdayNotifier:

    # instantiate with key and secret
    def __init__(self):
        pass

    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # new queue
    tweet_queue = Queue();

    # run
    while True:
        try:
            # get recent tweet
            tweet = api.GetUserTimeline(TWITTER_ID)
            # just get the recent one, ignore if user sends multiple tweets in less than 15 second span
            get_tweet_string = tweet[0].text

            # if the most recent tweet is in the queue, ignore
            if get_tweet_string in tweet_queue.items:
                print 'No new tweets.'
                # else tweet is not in the queue, add, display, and trim queue
            else:

                # display tweet in terminal
                print 'NEW TWEET COMING THROUGH: ' + get_tweet_string
                # enqueue
                tweet_queue.enqueue(get_tweet_string)

                # play alert
                pygame.mixer.init()
                pygame.mixer.music.load('sounds/eas.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

                # check if retweeted
                if tweet[0].retweeted_status:
                    tweet_wo_urls = re.sub(r'http\S+', '', 'The President just retweeted ' + get_tweet_string,
                                           flags=re.MULTILINE)
                else:
                    tweet_wo_urls = re.sub(r'http\S+', '', 'A new tweet from the President says ' + get_tweet_string,
                                           flags=re.MULTILINE)

                tts = gTTS(
                    text=tweet_wo_urls.encode('unicode_escape'),
                    lang='en')

                filename = 'temp.mp3'

                # save file with speech
                tts.save(filename)
                # play
                pygame.mixer.init()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
                # until stops playing
                while pygame.mixer.music.get_busy() == True:
                    continue
                # remove temporary file
                os.remove(filename)

                # trim queue (keep recent tweets only) in case of a tweet storm
                if tweet_queue.size() > QUEUE_SIZE:
                    # remove the oldest one
                    tweet_queue.dequeue()
        # for simplicity - broad exception
        except:
            # tell the user that there is a problem with connection
            filename = 'sounds/error-connection.mp3'

            print "There is a problem with internet connection or with twitter. Will try again in a few seconds."

            # print error message
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue

        # give twitter some time
        time.sleep(15)


if __name__ == "__main__":
    app = DoomsdayNotifier()
    app.run()
