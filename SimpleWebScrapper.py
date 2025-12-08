
import requests
from bs4 import BeautifulSoup
import csv

# Constants
BASE_URL = 'https://quotes.toscrape.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
OUTPUT_FILE = 'quotes.csv'  # Changed to relative path for portability


def fetch_page(url):
    """Fetch a page and return its BeautifulSoup object."""
    response = requests.get(url, headers=HEADERS)
    return BeautifulSoup(response.text, 'html.parser')


def extract_quotes_from_page(soup):
    """Extract all quotes from a BeautifulSoup page object."""
    quotes = []
    quote_elements = soup.find_all('div', class_='quote')
    
    for quote_element in quote_elements:
        # Get the text of the quote
        text = quote_element.find('span', class_='text').text.strip()
        
        # Get the author
        author = quote_element.find('small', class_='author').text.strip()
        
        # Get tags
        tag_elements = quote_element.find_all('a', class_='tag')
        tags = [tag.text for tag in tag_elements]
        
        # Append to the quotes list
        quotes.append({
            'text': text,
            'author': author,
            'tags': ', '.join(tags)
        })
    
    return quotes


def print_quotes(quotes):
    """Print quotes in a formatted way."""
    for quote in quotes:
        print(f"Quote: {quote['text']}")
        print(f"Author: {quote['author']}")
        print(f"Tags: {quote['tags']}")
        print("-" * 50)


def save_quotes_to_csv(quotes, filename):
    """Save quotes to a CSV file."""
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Text', 'Author', 'Tags'])
        
        for quote in quotes:
            writer.writerow(quote.values())


def scrape_all_quotes():
    """Scrape all quotes from all pages of the website."""
    all_quotes = []
    current_url = BASE_URL
    
    while current_url:
        # Fetch and parse the current page
        soup = fetch_page(current_url)
        
        # Extract quotes from the current page
        page_quotes = extract_quotes_from_page(soup)
        all_quotes.extend(page_quotes)
        
        # Find the next page link
        next_page = soup.find('li', class_='next')
        if next_page:
            next_page_relative_url = next_page.find('a', href=True)['href']
            current_url = BASE_URL + next_page_relative_url
        else:
            current_url = None
    
    return all_quotes


# Main execution
if __name__ == '__main__':
    # Scrape all quotes from all pages
    quotes = scrape_all_quotes()
    
    # Print the collected quotes
    print_quotes(quotes)
    
    # Save quotes to CSV file
    save_quotes_to_csv(quotes, OUTPUT_FILE)
    print(f"\nSaved {len(quotes)} quotes to {OUTPUT_FILE}")


