from pytwitter import Api
import json
import re
import os
import time
from dotenv import load_dotenv

load_dotenv()
api = Api(bearer_token=os.getenv("BEARER_TOKEN"))

oldTweet = os.getenv("OLDTWEET")
print(oldTweet)

while(True):
	res = api.search_tweets(query="Strangestone")
	for tweet in res.data:
		if "月曜日のたわわ　その" in tweet.text and oldTweet != tweet.text:
			print(tweet.text)
			fp = open("tweet", "w")
			fp.write(tweet.text)
			fp.close()
			os._exit(0)
		time.sleep(60)




