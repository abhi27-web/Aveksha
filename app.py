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
app = Flask(__name__)

def requestResults(user1,user2):
    nusers,wc,df=get_tweets(user1,user2)
    return nusers,wc,df

@app.route('/', methods=['POST', 'GET'])
def get_data():
    print(os.getcwd())
    if request.method == 'POST':        
        user1 = float(request.form['city1'])
        user2 = float(request.form['city2'])
        nusers,wc,df = requestResults(user1,user2)
        print(df['Analysis'].value_counts())
        plt.figure(figsize=(12,8))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        plt.plot()   
        plt.savefig('C:/Users/abhig/Downloads/DSCWOW/DSCWOW_Aveksha-main/DSCWOW_Aveksha/static/newplot1.png')
        plt.title('Sentiment Analysis')
        plt.xlabel('Sentiment')
        plt.ylabel('Counts')        
        df['Analysis'].value_counts().plot(kind = 'bar')  
        plt.savefig('C:/Users/abhig/Downloads/DSCWOW/DSCWOW_Aveksha-main/DSCWOW_Aveksha/static/newplot2.png')
        return render_template("Twitter_Today.html", column_names=nusers.columns.values, row_data=list(nusers.values.tolist()), zip=zip, url1 ='../static/newplot1.png', url2 ='../static/newplot2.png')
    return render_template("Twitter_Today.html")

if __name__ == '__main__':
    app.run(debug = False)


    