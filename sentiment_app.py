# sentiment_app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# 1. Scrape Headlines
# ----------------------------
def scrape_headlines():
    url = "https://www.npr.org/sections/news/"  # You can change to any blog/news site
    headlines = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: NPR headlines are inside <h2 class="title">
        titles = soup.find_all('h2', class_='title')

        for title in titles[:50]:  # Get top 50 if available
            headline = title.get_text(strip=True)
            if headline:
                headlines.append(headline)

    except Exception as e:
        st.error(f"Error while scraping: {e}")

    return headlines

# ----------------------------
# 2. Sentiment Analysis
# ----------------------------
def analyze_sentiment(headlines):
    results = []

    for headline in headlines:
        blob = TextBlob(headline)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        results.append({"Headline": headline, "Sentiment": sentiment})

    return pd.DataFrame(results)

# ----------------------------
# 3. Visualize
# ----------------------------
def plot_sentiment_distribution(df):
    sentiment_counts = df['Sentiment'].value_counts()
    st.subheader("Sentiment Distribution")

    chart_type = st.radio("Choose chart type:", ["Bar Chart", "Pie Chart"])

    if chart_type == "Bar Chart":
        st.bar_chart(sentiment_counts)
    else:
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

# ----------------------------
# 4. Streamlit UI
# ----------------------------
def main():
    st.title("📰 Sentiment Analyzer for News Headlines")

    if st.button("Scrape Headlines"):
        headlines = scrape_headlines()

        if not headlines:
            st.warning("No headlines found.")
            return

        df = analyze_sentiment(headlines)
        st.success(f"{len(df)} headlines analyzed!")
        st.dataframe(df)

        # Bonus: Filter by sentiment
        sentiment_filter = st.selectbox("Filter by Sentiment", options=["All", "Positive", "Negative", "Neutral"])
        if sentiment_filter != "All":
            df = df[df["Sentiment"] == sentiment_filter]
        
        st.write("### Filtered Headlines")
        st.dataframe(df)

        # Visualization
        plot_sentiment_distribution(df)

if __name__ == "__main__":
    main()
