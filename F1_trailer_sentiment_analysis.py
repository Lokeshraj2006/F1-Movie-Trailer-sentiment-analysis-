from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# To Download Comments
video_url = 'https://www.youtube.com/watch?v=69ffwl-8pCU'  # F1 Movie Trailer
downloader = YoutubeCommentDownloader()
comments = []

for comment in downloader.get_comments_from_url(video_url, sort_by=0):  # 0 = Top comments
    comments.append(comment['text'])

df = pd.DataFrame(comments, columns=['comment'])

# To filter and Clean Comments
def clean_comment(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^A-Za-z0-9\s]+", '', text)
    return text.lower()

df['cleaned_comment'] = df['comment'].apply(clean_comment)

# To perform Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['cleaned_comment'].apply(get_sentiment)

df.to_csv("f1_movie_comments.csv", index=False)  #To make a CSV file 

# To visualize Sentiment Distribution 
sentiment_counts = df['sentiment'].value_counts()
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
plt.title("Sentiment Distribution of F1 Movie Trailer Comments")
plt.show()

# To visualize Word Cloud
all_words = ' '.join(df['cleaned_comment'])
wc = WordCloud(width=800, height=400, background_color='black').generate(all_words)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Top Words in Comments")
plt.show()
