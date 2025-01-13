
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com/'

# Add headers for requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# List to store all quotes
quotes = []

# Find all quote blocks
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

# Print the collected quotes
for quote in quotes:
    print(f"Quote: {quote['text']}")
    print(f"Author: {quote['author']}")
    print(f"Tags: {quote['tags']}")
    print("-" * 50)

#for any next page 
next_page = soup.find('li',class_ = 'next')

#looping it

while next_page is not None:
    next_page_relative_url = next_page.find('a', href=True)['href']

    page = requests.get(url + next_page_relative_url,headers=headers)

    soup = BeautifulSoup(page.text,'html.parser')

    next_page = soup.find('li',class_ = 'next')

raw = r'C:\Users\Asus\OneDrive\Desktop\VS code\Github\quotes.csv' #add a file location here

with open(raw,'w',encoding = 'utf-8',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Text','Author','Tags'])

    for quote in quotes:
        writer.writerow(quote.values())

    csv_file.close()


