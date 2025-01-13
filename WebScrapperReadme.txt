Thanks To https://brightdata.com/blog/how-tos/web-scraping-with-python


# Quotes Scraper 📝

This Python project is a web scraper for extracting quotes, authors, and tags from the website [Quotes to Scrape](https://quotes.toscrape.com/). The extracted data is saved into a CSV file for further use.

---

## Features

- Scrapes quotes, authors, and tags from the website.
- Handles multiple pages of the website using pagination.
- Saves the scraped data into a CSV file in an organized format.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/quotes-scraper.git
   cd quotes-scraper
   ```

2. **Install Required Libraries**:
   Ensure you have Python installed. Then, install the necessary Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script**:
   ```bash
   python quotes_scraper.py
   ```

---

## Output

The script generates a CSV file containing the following fields:

- `Text`: The quote text.
- `Author`: The author of the quote.
- `Tags`: Tags associated with the quote.

### Example CSV Output
| Text                                                     | Author         | Tags                  |
|----------------------------------------------------------|----------------|-----------------------|
| "The world as we have created it is a process of our..." | Albert Einstein | change, deep-thoughts |
| "It is our choices, Harry, that show what we truly are..." | J.K. Rowling  | abilities, choices    |

The CSV file is saved at the following path (update as needed):  
`C:\Users\Asus\OneDrive\Desktop\VS code\Github\quotes.csv`

---

## Project Structure

```
quotes-scraper/
├── quotes_scraper.py  # The main Python script for scraping
├── requirements.txt   # Optional: List of dependencies
├── quotes.csv         # The generated CSV file (after running the script)
└── README.md          # Project documentation
```

---

## How It Works

1. **Scraping Quotes**:
   - The script starts at the main page of the website.
   - Extracts quotes, authors, and tags using BeautifulSoup.

2. **Pagination**:
   - Automatically navigates to the next page if available.
   - Repeats the scraping process until no more pages remain.

3. **Saving to CSV**:
   - All the scraped data is written to a CSV file.

---

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using:
```bash
pip install -r requirements.txt
```

---

## Contribution

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request. 😊



Feel free to adjust this README as needed for your GitHub repository! Let me know if you'd like help automating parts of this project.