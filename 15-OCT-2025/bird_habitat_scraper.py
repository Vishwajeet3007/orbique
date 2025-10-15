import requests
from bs4 import BeautifulSoup
import time

def scrape_all_about_birds():
    url = "https://www.allaboutbirds.org/news/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Retry mechanism
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Successfully fetched the page: {url}")
                soup = BeautifulSoup(response.text, "html.parser")

                # Find all bird-related news articles or species mentioned
                bird_data = []
                for article in soup.find_all("article"):
                    title = article.find("h2").get_text(strip=True)
                    summary = article.find("p").get_text(strip=True)
                    if "bird" in title.lower():
                        bird_data.append(f"Bird: {title}\nSummary: {summary}\n")

                return bird_data
            else:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
                time.sleep(2)  # Wait before retrying
        except Exception as e:
            print(f"Error fetching the page: {e}")
            time.sleep(2)  # Wait before retrying

    return []  # Return empty list if all retries fail

def scrape_birdlife_international():
    url = "https://www.birdlife.org/worldwide"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Successfully fetched the page: {url}")
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Extracting links to species or related information
        bird_data = []
        links = soup.find_all("a", href=True)
        for link in links:
            if "bird" in link.get_text().lower():  # Simplified check for bird-related content
                bird_data.append(f"Bird Link: {link.get('href')} - Text: {link.get_text(strip=True)}")

        return bird_data
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

def save_data_to_file(data, filename="15-OCT-2025/bird_data.txt"):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")

def main():
    print("Scraping data from All About Birds and BirdLife International...")

    # Scrape All About Birds website
    all_about_birds_data = scrape_all_about_birds()

    # Scrape BirdLife International website
    birdlife_data = scrape_birdlife_international()

    # Combine data
    combined_data = all_about_birds_data + birdlife_data

    # Save data to a text file
    save_data_to_file(combined_data)

    print("Data has been successfully saved to bird_data.txt")

if __name__ == "__main__":
    main()
