import tweepy
from googletrans import Translator, LANGCODES, LANGUAGES
import random
from time import sleep
import json

consumer_key = "YzNdOZf6LJM9RWRxh8JMMCOd7"
consumer_secret = "xgNduSLjdZME7pAzC8VEM52us7S5qRC8jkeELvrElzZD4445RT"
access_token = "1090333056844660738-8J6nDosbKVTlPs4D5QXMdu4KPJVup2"
access_token_secret = "YHFIU3sTJoaVBmdxzBei9ywHdD6CVUSaE5gDGkaedMH5v"

#login

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
last_id = ""
while(True):

    a = api.user_timeline(screen_name="realdonaldtrump", tweet_mode='extended')
    if(len(a) != 0):
        tweet = a[0].full_text
        if(last_id != a[0].id_str):
            url = ""
            print("--------------------------")
            print("original: " + tweet)
            #find if there is an url in the tweet
            if(tweet.find("http") != -1):
                index = tweet.index("http")
                url = tweet[index:]
                tweet = tweet[:index]
            #translation
            translator = Translator()
            lang1, lang2 = "en", ""
            for i in range(30):
                lang2 = random.choice(list(LANGUAGES.items()))[0]
                tweet = translator.translate(text=tweet, src=lang1, dest=lang2).text
                lang1 = lang2
            tweet = translator.translate(text=tweet, src=lang1, dest= 'en').text
            #if there is an url in the tweet
            if(url != ""):
                tweet = tweet + " " + url
            print("new: " + tweet)
            api.update_status(status="@realdonaldtrump " + tweet, in_reply_to_status_id=a[0].id_str)
            print("--------------------------")
            last_id = a[0].id_str
    sleep(10)