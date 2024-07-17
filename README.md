# Youtube-Video-Comments-Analytics

This is a Flask web application that scrapes comments from a YouTube video and performs sentiment analysis on the comments. The sentiments are categorized as positive, neutral, or negative, and the results are displayed as percentages.

## Features

- Scrape comments from a specified YouTube video
- Perform sentiment analysis on the comments using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Display the results of sentiment analysis in terms of percentages of positive, neutral, and negative comments

## Requirements

- Python 3.7+
- Flask
- Selenium
- Webdriver Manager
- NLTK (Natural Language Toolkit)
- Chrome WebDriver

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sujal369/Youtube-Video-Comments-Analytics.git
   cd Youtube-Video-Comments-Analytics

2. Install the required Python packages:


# Requirements
pip install -r requirements.txt
Create a requirements.txt file with the following content:

Flask
selenium
webdriver-manager
nltk
Download the NLTK VADER lexicon:

import nltk
nltk.download('vader_lexicon')

# Usage
Start the Flask application:

python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Enter the URL of the YouTube video you want to analyze and click the "Submit" button.

The application will scrape the comments, perform sentiment analysis, and display the results.

Project Structure
Copy code
yt-comments-sentiment-analysis/
├── templates/
│   └── index.html
├── app.py
└── requirements.txt
Code Overview
app.py: The main Flask application file that contains the code for scraping YouTube comments, performing sentiment analysis, and rendering the results.
templates/index.html: The HTML template for the web interface.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Flask
Selenium
NLTK
ChromeDriver
php
Copy code

In your `templates/index.html`, make sure you have the necessary form for input and to display the results:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Comments Sentiment Analysis</title>
</head>
<body>
    <h1>YouTube Comments Sentiment Analysis</h1>
    <form method="POST">
        <label for="video_url">YouTube Video URL:</label>
        <input type="text" id="video_url" name="video_url" required>
        <button type="submit">Submit</button>
    </form>
    
    {% if comments %}
        <h2>Results for {{ video_url }}</h2>
        <p>Positive Comments: {{ positive_percent }}%</p>
        <p>Neutral Comments: {{ neutral_percent }}%</p>
        <p>Negative Comments: {{ negative_percent }}%</p>
        
        <h3>Comments:</h3>
        <ul>
        {% for comment in comments %}
            <li>{{ comment }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
This README file provides a clear overview of the project, its features, requirements, installation instructions, usage, project structure, code overview, contribution guidelines, license, and acknowledgements. Feel free to customize it further as needed.
