import tweepy
import time
consumer_key = "##############################"
consumer_secret = "##############################"
access_token = "##############################"
access_token_secret = "##############################"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#-----Author : Kharfia Haithem -------------------------------------------------------------------------------#

import pandas as pd
username = 'Covid-19 OR Corona OR Covid OR Virus OR pandémie OR épidémie OR Coronavirus' #research tweet ,this is my exemple
count = 30
try:     
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 
 # Pulling information from tweets iterable object
 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)
print(tweets_df)
