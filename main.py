from matplotlib import patches
from textblob import  TextBlob
import sys, tweepy
import  matplotlib.pyplot as plt

def percentage(part,whole):
    return 100 * float(part)/float(whole)

consumerKey=""
consumerSecret=  ""
accessToken=""
accessTokenSecret=""

auth=tweepy.oAuthHandle(consumerKey, consumerSecret)
auth.set_acces_token("accessToken,accessTokenSecret")
api=tweepy.API(auth)

search=input("Enter the keyword/hashtag to search about: ")
searchterms=int(input("Tweets to analyze: "))

tweets=tweepy.Cursor(api.search, q=searchterms, lang="English").items(searchterms)
#date range can be added change documentation


#variables to store the polarity of tweets
positive=0
negative=0
neutral=0
polarity=0

for tweets in tweets:
    # print text of the tweet
    print(tweets.text)
    analyse=TextBlob(tweets.text)
    polarity += analyse.sentiment.polarity

    if analyse.sentiment.polarity == 0:
        neutral +=1
    elif analyse.sentiment.polarity < 0.00:
      negative += 1
    elif analyse.sentiment.polarity > 0.00:
        positive += 1

    positive= percentage(positive, searchterms)
    negative = percentage(negative, searchterms)
    neutral = percentage(neutral, searchterms)

    #2 decimal places

    print("People are tweeting on" + search + "by analyzing" + str(searchterms) + "tweets.")

    if polarity == 0:
        print("Neutral")
    elif polarity < 0:
        print("Negative")
    elif polarity > 0:
        print("Positive")

        #piechart

        labels=['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 'Neutral ['+str(neutral)+'%]']
        sizes = [positive, neutral, negative]
        colors = ['green', 'blue', 'red']
        patches, texts = plt.pie(sizes, colors=colors, startangle=0)
        plt.legend(patches, labels, loc="best")
        plt.title("People are tweeting on" + search + "by analyzing" + str(searchterms) + "tweets.")
        plt.axis('equal')
        plt.tight_layout()