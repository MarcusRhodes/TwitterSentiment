#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:51:11 2020

@author: marcus
"""

import os
import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key=os.environ.get("YOUR_CONSUMER_KEY"),
                        consumer_secret=os.environ.get("YOUR_CONSUMER_SECRET"),
                        access_token_key=os.environ.get("YOUR_ACCESS_TOKEN_KEY"),
                        access_token_secret=os.environ.get("YOUR_ACCESS_TOKEN_SECRET"))

# test authentication
print(twitter_api.VerifyCredentials())


def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])