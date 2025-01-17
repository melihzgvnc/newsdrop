import os
import tweepy

os.environ["CONSUMER_KEY"] = os.getenv("CONSUMER_KEY")
os.environ["CONSUMER_SECRET"] = os.getenv("CONSUMER_SECRET")
os.environ["ACCESS_TOKEN"] = os.getenv("ACCESS_TOKEN")
os.environ["ACCESS_TOKEN_SECRET"] = os.getenv("ACCESS_TOKEN_SECRET")

class Publisher:

    client = tweepy.Client(
        consumer_key=os.environ["CONSUMER_KEY"],
        consumer_secret=os.environ["CONSUMER_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    )

    def __init__(self, insights, links):
        
        self.tweets = self.make_ready_to_publish(zip([insights], [links]))
        
    
    def make_ready_to_publish(self, tweets):
        
        for news, link in tweets:
            yield (news, link)


    def publish(self):
        insight, link = next(self.tweets)
        tweet_main = self.client.create_tweet(text=insight)
        tweet_ref = self.client.create_tweet(text=link, in_reply_to_tweet_id=tweet_main.data.id)
        
        print("Tweets have been successfully published!")