# app.py

#  Import the necessary tools
import streamlit as st  # For UI and interactivity
import pandas as pd  # To work with CSV data
from collections import Counter  # To count word frequencies
import matplotlib.pyplot as plt  # To make bar charts
from wordcloud import WordCloud  # To make word clouds
import re  # For regular expressions
import string  # To remove punctuation
from nltk.corpus import stopwords  # For removing common words like 'the', 'is', etc.
import nltk  # Natural Language Toolkit for text processing

#  Download stopwords (only runs once)
nltk.download('stopwords')

#  Load headlines from the CSV file
@st.cache_data  # Cache the result for faster reload
def load_data():
    return pd.read_csv("headlines.csv")

df = load_data()

#  Function to clean and split each headline into useful words
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    words = text.split()  # Split into words
    stop_words = set(stopwords.words("english"))  # Load stopwords
    return [word for word in words if word not in stop_words]  # Remove them

#  Count how often each word appears
all_words = []
for headline in df['headline']:
    all_words.extend(clean_text(headline))  # Add cleaned words to the list

word_freq = Counter(all_words)  # Count word frequency
top_keywords = word_freq.most_common(5)  # Get top 5 trending keywords

#  Streamlit User Interface
st.title(" Trending Topics Extractor")
st.write("### Top 5 Keywords Based on News Headlines:")

#  Show top 5 keywords
for word, freq in top_keywords:
    st.write(f"🔹 **{word}** – {freq} times")

#  Chart Selection: Bar or Word Cloud
chart_type = st.radio("Choose a chart type to visualize:", ["Bar Chart", "Word Cloud"])

if chart_type == "Bar Chart":
    # Create a bar chart
    words, counts = zip(*top_keywords)
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_ylabel("Frequency")
    ax.set_title("Top 5 Keywords")
    st.pyplot(fig)

elif chart_type == "Word Cloud":
    # Create a word cloud
    wc = WordCloud(width=600, height=300, background_color='white').generate_from_frequencies(dict(top_keywords))
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

# 🔍 Search functionality
st.write("### 🔍 Search Headlines by Keyword")
search = st.text_input("Enter a keyword to find matching headlines:")

# Display results
if search:
    result_df = df[df['headline'].str.contains(search, case=False, na=False)]
    st.write(f"Found {len(result_df)} matching headlines:")
    for i, row in result_df.iterrows():
        st.write(f"• {row['headline']}")
