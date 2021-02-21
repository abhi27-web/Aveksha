import matplotlib.pyplot as plt
import os
from textblob import TextBlob
from wordcloud import WordCloud
from flask import Flask, render_template, redirect, request
from tweet import getSubjectivity
from tweet import getPolarity
from tweet import getAnalysis
from tweet import clean
from tweet import scraptweets
from tweet import get_tweets
from datetime import date
from datetime import datetime
app = Flask(_name_)

def requestResults(user1,user2):
    nusers,wc,df,todayGraph=get_tweets(user1,user2)
    return nusers,wc,df,todayGraph

@app.route('/', methods=['POST', 'GET'])
def get_data():
    print(os.getcwd())
    if request.method == 'POST':      
        user1 = float(request.form['city1'])
        user2 = float(request.form['city2'])
        nusers,wc,df,todayGraph = requestResults(user1,user2)
        print(df['Analysis'].value_counts())
        plt.figure(figsize=(12,8))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        plt.plot()  
        today = datetime.now().strftime("%Y%m%d-%H%M%S")
        plt.savefig('./static/{}.png'.format(today))
        # plt.title('Sentiment Analysis')
        # plt.xlabel('Sentiment')
        # plt.ylabel('Counts')        
        # df['Analysis'].value_counts().plot(kind = 'bar')  
        # # plt.show()
        # plt.savefig('C:/Users/abhig/Downloads/DSCWOW/DSCWOW_Aveksha-main/DSCWOW_Aveksha/static/newplot2.png')
        return render_template("about.html", isLoggedin=1,column_names=nusers.columns.values, row_data=list(nusers.values.tolist()), zip=zip, url1 ='./static/{}.png'.format(today), url2 ='./static/Graph{}.png'.format(todayGraph))
    return render_template("about.html",isLoggedin=1)

if _name_ == '_main_':
    app.run(debug = False)