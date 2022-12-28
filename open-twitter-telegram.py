import random
import base64
import requests 
import json 
import time
import tweepy
from easychatgpt import ChatClient
import os
from dotenv import load_dotenv



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from GoogleNews import GoogleNews
googlenews = GoogleNews()

## make sure to have a .env file with your openai email and password in the directory of this script's location.
load_dotenv()
OPENAI_EMAIL = os.getenv("OPENAI_EMAIL")
OPENAI_PASSWORD = os.getenv("OPENAI_PASSWORD")

chat = ChatClient(OPENAI_EMAIL,OPENAI_PASSWORD)


## tweet the most recent news story based on the result of the google news search
def tweet():


   
  ## authenticate with twitter v2 api
    consumer_key = ""
    consumer_secret = ""
    bearer_token = ""

    access_token = ""
    access_token_secret = ""

    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)










    hashtags = "(HASHTAGS HERE)"
    search = "(SEARCH HERE)"

    googlenews = GoogleNews()
    googlenews.search(search)
    result = googlenews.result()

    print(result)

    user = input("Enter a story number:  ")
    user_int = int(user) 
    ### allow the user to select the news story they want to tweet
    

    title = result[user_int]['title']
    url = result[user_int]['link']

    answer = chat.interact(f"Generate a short summary tweet about the most recent news stories I will be sending you. Here is the first one. Generate a hashtag for the article. Always include the hashtag #(yourhashtag) & #breaking - {title} {url} ")

    print(answer)





    ### create a variable containing the title and url of the most recent news story
    
    content = (f"{answer} {url}")

    ## tweet the most recent news story
    response = client.create_tweet(text=content)

   


  
    tweet_id= (f"https://twitter.com/user/status/{response.data['id']}")
    updater = Updater
    updater = Updater(token='(TG_TOKEN_HERE)', use_context=True)
    dispatcher = updater.dispatcher 
    updater.bot.send_message(chat_id='(CHAT_ID_HERE)', text=tweet_id)
    ## send message to group id or userid. 
    googlenews.clear()

  



while True:
    tweet()
    time.sleep(60 * 5)
