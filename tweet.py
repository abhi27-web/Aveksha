import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.stem import PorterStemmer
nltk.download('punkt')
from collections import Counter
import re
import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

def clean(db_tweets):
    dataset=pd.DataFrame(columns = ['username','location', 'text', 'hashtags'])
    dataset =db_tweets
    dataset['text'].isna().sum() 
    dataset['clean_tweet'] = dataset['text'].apply(lambda x: ' '.join([tweet for tweet in x.split() if not tweet.startswith("@")]))
    dataset['clean_tweet'] = dataset['clean_tweet'].apply(lambda x: ' '.join([tweet for tweet in x.split() if not tweet.isnumeric()]))
    slang = {'luv':'love','wud':'would','lyk':'like','wateva':'whatever','ttyl':'talk to you later',
              'kul':'cool','fyn':'fine','omg':'oh my god!','fam':'family','bruh':'brother', 'cud':'could',
             'fud':'food', 'u':'you', 'ur':'your', 'frm': 'from'}
    dataset['clean_tweet'] = dataset['clean_tweet'].apply(lambda x : ' '.join(slang[word] if word in slang else word for word in x.split()))
    dataset['Hashtags'] = dataset['clean_tweet'].apply(lambda x : ' '.join([word for word in x.split() if word.startswith('#')]))
    dataset.drop('text',axis=1,inplace=True)
    #dataset.drop('hashtags',axis=1,inplace=True)
    dataset['clean_tweet'] = dataset['clean_tweet'].apply(lambda x : ' '.join([word for word in x.split() if not word in set(stopwords.words('english'))]))
    lemmatizer = WordNetLemmatizer()
    dataset['clean_tweet'] = dataset['clean_tweet'].apply(lambda x : ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))
    ps = PorterStemmer()
    dataset['clean_tweet'] = dataset['clean_tweet'].apply(lambda x : ' '.join([ps.stem(word) for word in x.split()]))
    dataset['text']=dataset['clean_tweet']
    dataset.drop('clean_tweet',axis=1,inplace=True)
    dataset['Subjectivity'] = dataset['text'].apply(getSubjectivity)
    dataset['Polarity'] = dataset['text'].apply(getPolarity)
    dataset['Analysis'] = dataset['Polarity'].apply(getAnalysis)
    nusers = dataset[dataset.Analysis == 'Negative']
    df=dataset
    allWords = ' '.join([twts for twts in df['text']])
    new_stopwords=["woman","women","girl","women'","https"]
    wc = WordCloud(width = 800, height = 500, max_font_size = 110, max_words=100, stopwords=new_stopwords).generate(allWords)
    ax = df['Analysis'].value_counts().plot(kind = 'bar')
    fig = ax.get_figure()
    fig.savefig('C:/Users/abhig/Downloads/DSCWOW/DSCWOW_Aveksha-main/DSCWOW_Aveksha/static/newplot2.png')
    return nusers,wc,df

def scraptweets(search_words,numTweets,latitude,longitude):
    
    
    consumerKey = "1dxddKBUmRCr8g0YDp3VeTTvK"
    consumerSecretKey = "g5g2Wa6Xsc7uQMvnOBfK1iHz0OTtbqtS7IaP5PCIK39MCfaj7Q"
    accessToken = "962006996055502848-pXTUZdYfqcHd2LBU73ONGLepJXFh2tn"
    accessTokenSecret = "OLxYCAcXl206ZgNcQGhsuJcuaXCdWWSLDV2VMwK51tUVK"

    # consumerKey = "Ts7w6URgOYWXRfNuJwiUVoSz4"
    # consumerSecret = "iqItFdmQ84UtcMT7PDIx9Ygovjzd6PW4akEI27Q6MUmqIrbjaR"
    # accessToken = "1171293910175383554-17noADblkdWPPDVSYTXtyAIPsFsAqp"
    # accessTokenSecret = "MVUeVZQz0QkFbVcHTaKkusAZNK0RQf5qDvIlVjopYfL9G"
    # Create the authentication object
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecretKey) 
        
    # Set the access token and access token secret
    authenticate.set_access_token(accessToken, accessTokenSecret) 
        
    # Creating the API object while passing in auth information
    api = tweepy.API(authenticate, wait_on_rate_limit = True)
    db_tweets = pd.DataFrame(columns = ['username','location', 'text', 'hashtags'])
    for i in range(0, 1):
        tweets = tweepy.Cursor(api.search, lang="en",q=search_words, geocode="%f,%f,%dkm" % (latitude, longitude, 100), tweet_mode='extended').items(numTweets)
        tweet_list = [tweet for tweet in tweets]
    for tweet in tweet_list:
        username = tweet.user.screen_name
        location = tweet.user.location
        hashtags = tweet.entities['hashtags']
        try:
            text = tweet.retweeted_status.full_text
        except:  # Not a Retweet
            text = tweet.full_text
            ith_tweet = [username, location, text, hashtags]
            db_tweets.loc[len(db_tweets)] = ith_tweet
    return clean(db_tweets)

def get_tweets(user1,user2):
    # data = pd.read_csv('Data.csv')
    # data.drop(data.columns[[3,4,5]], axis = 1, inplace = True) 
    search_words = "women"
    # data['City'] = data['City'].apply(lambda x: x.lower())
    latitude= user1
    longitude = user2
    return scraptweets(search_words,100,latitude,longitude)
     