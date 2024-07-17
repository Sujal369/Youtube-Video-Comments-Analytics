from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

app = Flask(__name__)

# Download NLTK VADER lexicon
import nltk
nltk.download('vader_lexicon')

# Initialize VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Function to scrape YouTube comments and perform sentiment analysis
def get_youtube_comments(video_url, scrolls=10, delay=2):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(video_url)
        time.sleep(delay)

        for _ in range(scrolls):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(delay)

        comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        comments = [comment.text for comment in comment_elements]
    
    finally:
        driver.quit()

    return comments

def analyze_sentiment(comment):
    scores = sid.polarity_scores(comment)
    compound = scores['compound'] *10
    if compound >= 0.5:
        return 'positive'
    elif compound <= -0.5:
        return 'negative'
    else:
        return 'neutral'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        comments = get_youtube_comments(video_url)
        # Analyze sentiment for each comment and count results
        sentiment_counts = {'positive': 0, 'neutral': 0, 'negative': 0}
        for comment in comments:
            sentiment = analyze_sentiment(comment)
            sentiment_counts[sentiment] += 1
        
        # Calculate percentages
        total_comments = len(comments)
        positive_percent = (sentiment_counts['positive'] / total_comments) * 100
        neutral_percent = (sentiment_counts['neutral'] / total_comments) * 100
        negative_percent = (sentiment_counts['negative'] / total_comments) * 100

        return render_template('index.html', video_url=video_url, comments=comments, 
                               positive_percent=positive_percent, neutral_percent=neutral_percent,
                               negative_percent=negative_percent)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)