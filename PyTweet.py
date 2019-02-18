
#-----------------------------------------------------------------------#
# AUTHOR         : Ankit Vashistha                                      #
# SCRIPT         : pytweet v0.6                                         #
# REQUIRED       : tweepy, tc, pandas, numpy, matplotlib, textblob, re  #
# PYTHON VERSION : 3.5+                                                 #
# PRE-REQUISITES : Twitter Account, Twitter App, App Auth Details       #
#-----------------------------------------------------------------------#

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

#### TWITTER CLIENT ####
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client
    
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
        
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
        
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


#### TWITTER AUTHENTICATOR ####
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET) # Authenticate our credentials
        auth.set_access_token(tc.ACCESS_TOKEN, tc. ACCESS_TOKEN_SECRET) # Complete the Authentication process.
        return auth


#### TWITTER STREAMER ####
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_file, hash_tag_list): # File stores the fetched tweets, hashtag list of keywords to filter tweets.
        listener = TwitterListener()  # Create Object of the class created above inherited from StreamListener class.
        auth = self.twitter_authenticator.authenticate_twitter_app()

        stream = Stream(auth, listener) # Fetch stream of tweets by passing auth and listener objects.

        # Filter the stream based on the specified keywords.
        stream.filter(track=hash_tag_list)


#### TWITTER LISTENER ####
class TwitterListener(StreamListener):
    """
    Basic listener class that prints received tweets to Standard Out.
    """
    def __init__(self,fetched_tweets_file):
        self.fetched_tweets_file = fetched_tweets_file

    def on_data(self, data):  # Takes data from StreamListener which listens to tweets.
        try:
            #print(f'Data Filtered: {data}')
            with open(self.fetched_tweets_file, 'a') as tf:
                tf.write(data)
            return True
            
        except BaseException as e:
            print(f'Error Occured is: {e}')
            
        return True

    def on_error(self, status):
        if status == 420:
            # Returning Flase in case the rate limit is reached.
            return False
        print(f'An error occured: {status}') # Prints Error if any Error occured.


#### TWEETS ANALYZER ####
class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """
    
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
            
        elif analysis.sentiment.polarity == 0:
            return 0
            
        else:
            return -1
    
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])
        
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['coordinates'] = np.array([tweet.coordinates for tweet in tweets])
        df['geo'] = np.array([tweet.geo for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['place'] = np.array([tweet.place for tweet in tweets])
        
        return df
        
if __name__ == "__main__":  # Main of Program
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    
    api = twitter_client.get_twitter_client_api()
    
    tweets = api.user_timeline(screen_name="", count=50) # Update twitter handle name
        
    df = tweet_analyzer.tweets_to_data_frame(tweets)

    df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
    
    print(df.head(10)) # First 10 entries in the DataFrame
