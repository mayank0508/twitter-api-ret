import tweepy
import time

auth = tweepy.OAuthHandler('ofVW1WX28hsxh1bveZaA5FhGh','Qj8RRTD4jDcjY5ELoACS3FQzMWtZ5i03nT6pQT6qluLUEoir37')

auth.set_access_token('1360279899433410562-N4zoHGhWKQ5GZVH9maZ45Zuqja5jdO', 'szyC5Jtt76pyzgxR5USASwcuFDjKQZiXo2MJpckIKwWCR')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)