import gatherIndividualTweets
import tweepy
import random

def getAllTweets(firstTweets, secondTweets):
  allTweets = []
  for tweet in firstTweets:
    allTweets.append(tweet)
  for tweet in secondTweets:
    allTweets.append(tweet)
  return allTweets

def guessTheTweet():

  firstScreenName = input('Enter the twitter handle of the first person you want to play with: ')
  secondScreenName = input('Enter the twitter handle of the second person you want to play with: ')

  setOneTweets = gatherIndividualTweets.getFirstTweets(firstScreenName)
  setTwoTweets = gatherIndividualTweets.getSecondTweets(secondScreenName)
  totalTweets = getAllTweets(setOneTweets, setTwoTweets)
  totalGuesses = 0
  correctGuesses = 0
  seenTweets = []
  while totalGuesses < len(totalTweets):
    randomTweet = random.choice(totalTweets)
    if randomTweet not in seenTweets:
      print("Guess who the following tweet is from by inputting the user screen name: ")
      print(randomTweet)
      userGuess = input("Guess: ").lower().strip()
      if (userGuess == firstScreenName) and (randomTweet in setOneTweets):
        print("Correct! That was a " + firstScreenName + " tweet! Keep going now!")
        totalGuesses += 1
        correctGuesses += 1
      elif (userGuess == secondScreenName) and (randomTweet in setTwoTweets):
        print("Correct! That was a " + secondScreenName + " tweet! Keep going now!")
        totalGuesses += 1
        correctGuesses += 1
      else:
        print("Incorrect. You got that one wrong, but keep going!")
        totalGuesses += 1
      seenTweets.append(randomTweet)
  print("You're done! Your accuracy is guessing the tweets was " + str(correctGuesses/totalGuesses))


guessTheTweet()