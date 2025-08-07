# scraper.py

# 📦 Import the libraries needed
import requests  # to send a request to the website
from bs4 import BeautifulSoup  # to extract content from HTML
import pandas as pd  # to store and save headlines

# 📌 Function to scrape headlines from Inshorts
def scrape_inshorts():
    url = 'https://inshorts.com/en/read'  # Inshorts main page (English)
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # 📰 Find all article headlines
    headlines = []
    for span in soup.find_all('span', itemprop='headline'):
        headlines.append(span.text.strip())  # Clean each headline

    # 💾 Save the headlines into a CSV file
    df = pd.DataFrame({'headline': headlines})
    df.to_csv('headlines.csv', index=False)

    print(f"✅ Scraped {len(headlines)} headlines and saved to 'headlines.csv'")

# ▶️ Run the function when this file is executed directly
if __name__ == "__main__":
    scrape_inshorts()
