import json
import requests
import json
import re
import os
import time
from dotenv import load_dotenv

# Load env
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")
chatid = os.getenv("CHATID")

def bearer_oauth(r):

	r.headers["Authorization"] = f"Bearer {bearer_token}"
	r.headers["User-Agent"] = "v2FilteredStreamPython"
	return r

def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    #print(json.dumps(response.json()))
    return response.json()

def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    #print(json.dumps(response.json()))

def set_rules(delete):
	sample_rules = [
    	{"value": "月曜日のたわわ　その from:Strangestone OR from:WeiWeiDev"},
	]
	payload = {"add": sample_rules}
	response = requests.post(
		"https://api.twitter.com/2/tweets/search/stream/rules",
		auth = bearer_oauth,
		json = payload,
	)
	if response.status_code != 201:
		raise Exception(
			"Cannot add rules : {} {}".format(response.status_code, response.text)
		)
	#print(json.dumps(response.json()))

def get_stream(set):
	tweet_fields = "tweet.fields=public_metrics,entities"
	url = "https://api.twitter.com/2/tweets/search/stream?{}&expansions=author_id".format(tweet_fields)
	response = requests.get(
		url,auth=bearer_oauth, stream=True,
	)
	#print(response.status_code)
	if response.status_code != 200:
		raise Exception(
			"Cannot add stream, : {} {}".format(response.status_code, response.text)
		)
	for response_line in response.iter_lines():
		if response_line:
			json_response = json.loads(response_line)
			# print(json.dumps(json_response, indent=4, sort_keys=True))
			if "RT " not in json_response["data"]["text"] and "月曜日のたわわ　その" in json_response["data"]["text"]:
				print(json_response["data"]["text"])
				apiurl = 'https://api.telegram.org/bot5205675326:AAHRYduNrmmybdlWYftk64ostssY833RVtQ/'
				telemethod = "sendMessage"
				chat_id = chatid
				content = "注意"
				urlm = '%s%s?chat_id=%s&text=%s' % (apiurl,telemethod,chat_id,content) #messangeurl
				r = requests.get(urlm)
				content = json_response["data"]["text"]
				urlm = '%s%s?chat_id=%s&text=%s' % (apiurl,telemethod,chat_id,content) #messangeurl
				r = requests.get(urlm)
				os._exit(0)

def main():
	rules = get_rules()
	delete = delete_all_rules(rules)
	set = set_rules(delete)
	get_stream(set)

if __name__ == "__main__":
	main()

#printer.filter(follow=['993160436001292288', '518677431', '93332575', '1501443423026708481'])


'''
# streaming_client = tweepy.StreamingClient(bearer_token)
class TweetPrinter(tweepy.StreamingClient):

	def on_tweet(self, tweet):
		if "RT " not in tweet.text:
			print(tweet.text)
			os._exit(0)
		#if "RT " not in tweet.text and "月曜日のたわわ" in tweet.text and "その" in tweet.text: 
		#	print(tweet.text)
		#	os._exit(0)

printer = TweetPrinter(bearer_token)
#printer.add_rules(tweepy.StreamRule("@strangestone"))
#printer.add_rules(tweepy.StreamRule("@wiwi571246"))
#printer.filter()
#printer.add_rules(tweepy.StreamRule("@WeiWeiDev"))
printer.filter()
'''



'''
oldTweet = os.getenv("OLDTWEET")
print(oldTweet)

while(True):
	res = api.search_tweets(query="Strangestone")
	for tweet in res.data:
		if "RT " not in tweet.text and "月曜日のたわわ　その" in tweet.text and oldTweet != tweet.text:
			print(tweet.text)
			fp = open("tweet", "w")
			fp.write(tweet.text)
			fp.close()
			os._exit(0)
		time.sleep(60)
'''