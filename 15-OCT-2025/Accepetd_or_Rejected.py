import requests
from bs4 import BeautifulSoup

# Step 1: Scrape the URL to extract article titles and prices
url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting article data (titles and prices)
articles = []
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color').text.strip()  # Get price and strip whitespace
    price = price.replace('Â', '').replace('£', '').strip()  # Remove unwanted characters and symbols
    try:
        articles.append((title, float(price)))  # Convert to float
    except ValueError as e:
        print(f"Error converting price for '{title}': {e}")

# Step 2: Save the data to a text file
with open('15-OCT-2025/articles_data.txt', 'w') as file:
    for title, price in articles:
        file.write(f"Title: {title} | Price: £{price}\n")

# Step 3: Import the data into a dictionary
articles_dict = {title: price for title, price in articles}

# Step 4: Calculate the total number of articles and the total cost
total_articles = len(articles_dict)
total_cost = sum(articles_dict.values())

# Step 5: Display status based on price (e.g., rejecting if above £30)
X = 30  # Example threshold, you can change this amount
status = {}
for title, price in articles_dict.items():
    if price > X:
        status[title] = 'REJECTED'
    else:
        status[title] = 'ACCEPTED'

# Output results
print(f"Total Articles: {total_articles}")
print(f"Total Cost: £{total_cost:.2f}")
print("Article Status:")
for title, stat in status.items():
    print(f"{title}: {stat}")
