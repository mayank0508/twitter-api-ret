import tweepy
import time

auth = tweepy.OAuthHandler('ofVW1WX28hsxh1bveZaA5FhGh','Qj8RRTD4jDcjY5ELoACS3FQzMWtZ5i03nT6pQT6qluLUEoir37')

auth.set_access_token('1360279899433410562-N4zoHGhWKQ5GZVH9maZ45Zuqja5jdO', 'szyC5Jtt76pyzgxR5USASwcuFDjKQZiXo2MJpckIKwWCR')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'bitcoin'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
       print('Tweet Retweeted')
       tweet.retweet()
       time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
            break   