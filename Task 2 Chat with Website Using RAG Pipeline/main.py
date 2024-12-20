import requests
from bs4 import BeautifulSoup
import time
from query_processor import QueryProcessor  # Importing QueryProcessor class

# Updated function for scraping websites with retry and delay mechanism
def scrape_website(url, retries=3, delay=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        content = []
        paragraphs = soup.find_all('p')
        for para in paragraphs:
            content.append(para.get_text())

        title = soup.title.string if soup.title else "No title found"

        scraped_data = [{'title': title, 'url': url, 'content': ' '.join(content)}]
        return scraped_data

    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(f"Error scraping {url}: {e}")
        if retries > 0:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
            return scrape_website(url, retries-1, delay)
        return []

# Main function for scraping data from multiple websites and handling queries
def main():
    urls = [
        'https://www.stanford.edu/',
        'https://und.edu/',
        'https://www.uchicago.edu/',
        'https://www.washington.edu/'
    ]

    scraped_data = []

    # Scrape data from all URLs
    for url in urls:
        print(f"Scraping content from {url} ...")
        data = scrape_website(url)
        scraped_data.extend(data)
        print(f"Successfully scraped {len(data)} records from {url}\n")

    # Instantiate the QueryProcessor with the scraped data
    query_processor = QueryProcessor(scraped_data)

    # Ask for user query
    query = input("Enter your query: ")

    # Perform search
    results = query_processor.search(query)

    # Display results
    if results:
        for result in results:
            print(f"Found result: {result['title']}")
            print(f"URL: {result['url']}")
            print(f"Content: {result['content'][:200]}...")  # Print a snippet of the content
            print("\n" + "-"*50 + "\n")
    else:
        print(f"No results found for '{query}'.")

if __name__ == "__main__":
    main()
