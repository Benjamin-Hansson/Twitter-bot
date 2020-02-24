import tweepy
from googletrans import Translator, LANGCODES, LANGUAGES
import random
from config import consumer_key, consumer_secret, access_token, access_token_secret

from time import sleep
import json

# login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
last_id = ""

while (True):
	a = api.user_timeline(screen_name="realdonaldtrump", tweet_mode='extended')

	if a and a[0].id_str != last_id:
			translator = Translator()

			tweet = a[0].full_text
			print("---------------------------")
			print("Tweet:", tweet)

			# & seems to crash the translator
			tweet = tweet.replace("&", "and ")

			# Preserve the url if there is one
			index = tweet.find("http")
			url = ""
			if index != -1:
				url = tweet[index:]
				tweet = tweet[:index]
				print(index)

			if not tweet:
				continue
			# Translate 30 times (100 takes to long time and there is a limit on number of requests to the api)
			# Idea still the same though
			lang1, lang2 = "en", ""

			for i in range(30):
				lang2 = random.choice(list(LANGUAGES.items()))[0] # choose a random language
				tweet = translator.translate(text=tweet, src=lang1, dest=lang2).text
				lang1 = lang2

			tweet = translator.translate(text=tweet, src=lang1, dest='en').text # translate back to english
			tweet = tweet + " " + url # add back the url
			print("new: " + tweet)

			api.update_status(status="@realdonaldtrump " + tweet, in_reply_to_status_id=a[0].id_str)
			last_id = a[0].id_str
			sleep(100)
	# print("--------------------------")

