import tweepy
import time

auth = tweepy.OAuthHandler('H6gFo3kndfuxJJkxO9c38nN6X','jLbhFvYvp12WZ1Co9bysn52y8TkVKAujRaESIr7UnJKdGkaETd')

auth.set_access_token('1360279899433410562-AOrLTpmqRprwcnEIoBwvU1MZwTlEVY', 'jtmOu9zeVWucUiB168ToGYmPeGBTR1FiQYGokJaxdytWG')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'bitcoin'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
       print('Tweet Retweeted')
       tweet.retweet()
       time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
            break   