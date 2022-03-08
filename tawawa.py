# pip install python-twitter-v2
from pytwitter import Api
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
api = Api(bearer_token=os.getenv("BEARER_TOKEN"))

# res = api.get_users(usernames="Strangestone")
# print(res)

res = api.search_tweets(query="Strangestone")
print(type(res))
for tweet in res.data:
	if "RT " not in tweet.text and "月曜日のたわわ　その" in tweet.text:
		print(tweet.text)
		fp = open("tweet", "w")
		fp.write(tweet.text)
		fp.close()

#res = api.get_tweets("1500685768385531911")
#if "RT " not in str(res.data[0].text) and "月曜日のたわわ　その" in str(res.data[0].text):
#	print(res.data[0].text)
#	print(re.search("(?P<url>https?://[^\s]+)", res.data[0].text).group("url"))
#	fp = open("tweet", "w")
#	fp.write(res.data[0].text)
#	fp.close()
#


