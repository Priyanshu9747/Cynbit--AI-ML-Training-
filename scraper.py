import requests
from bs4 import BeautifulSoup
import pandas as pd

all_data = []

for page in range(1, 6):  # First 5 pages
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for q in quotes:
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        tags = [tag.text for tag in q.find_all('a', class_='tag')]
        all_data.append({"quote": text, "author": author, "tags": ', '.join(tags)})

df = pd.DataFrame(all_data)
df.to_csv('quotes.csv', index=False)

import streamlit as st
import pandas as pd

st.title("📜 Quotes Explorer")
df = pd.read_csv('quotes.csv')

search = st.text_input("Search quotes or authors")
if search:
    filtered = df[df['quote'].str.contains(search, case=False) | df['author'].str.contains(search, case=False)]
    st.write(filtered)
else:
    st.write(df)
