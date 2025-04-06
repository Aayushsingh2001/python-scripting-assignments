import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <h2> elements
        titles = soup.find_all('h2')

        print(f"\nFound {len(titles)} titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Cloud_computing"  # add any public website
    scrape_titles(url)
