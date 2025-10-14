import requests
from bs4 import BeautifulSoup
import csv

# Target website
URL = 'http://books.toscrape.com/'

# Send GET request
response = requests.get(URL)

# Check for success
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    # Open CSV file for writing
    with open('14OCT2025/books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price'])  # Header row

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            writer.writerow([title, price])

    print("✅ Data saved to books.csv")
else:
    print(f"❌ Failed to retrieve content: Status code {response.status_code}")
