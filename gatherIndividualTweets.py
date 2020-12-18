import Keys
import tweepy

def getFirstTweets(firstScreenName):
  auth = tweepy.OAuthHandler(Keys.getConsumerKey, Keys.getConsumerKeySecret)  
  auth.set_access_token(Keys.getAccessToken, Keys.getAccessTokenSecret) 

  api = tweepy.API(auth) 

  tweets = api.user_timeline(firstScreenName, exclude_replies=True, include_rts=False, count=3200) 
  
  firstT=[]  
  
  tweetsByFirst = [tweet.text for tweet in tweets]
  for j in tweetsByFirst: 
    firstT.append(j)  
  return (firstT) 


def getSecondTweets(secondScreenName):
  auth = tweepy.OAuthHandler(Keys.getConsumerKey, Keys.getConsumerKeySecret)  
  auth.set_access_token(Keys.getAccessToken, Keys.getAccessTokenSecret) 

  api = tweepy.API(auth) 
  
  tweets = api.user_timeline(secondScreenName, exclude_replies=True, include_rts=False, count=3200) 
  
  secondT=[]  
  
  tweetsBySecond = [tweet.text for tweet in tweets] 
  for t in tweetsBySecond: 
    secondT.append(t)  
  return (secondT) 

def getAllTweets(firstTweets, secondTweets):
  allTweets = []
  for tweet in firstTweets:
    allTweets.append(tweet)
  for tweet in secondTweets:
    allTweets.append(tweet)
  return allTweets
