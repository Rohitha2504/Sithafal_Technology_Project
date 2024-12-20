import requests
from bs4 import BeautifulSoup

# Scrape website function
def scrape_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        # Send a GET request to the website with the User-Agent header
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an exception for bad responses (4xx, 5xx)

        # Parse the content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data - this will depend on the website structure
        content = []
        
        # Extract the main text content (all paragraphs)
        paragraphs = soup.find_all('p')  # Find all paragraph elements
        for para in paragraphs:
            content.append(para.get_text())

        # Extract the title of the page
        title = soup.title.string if soup.title else "No title found"
        
        # Format the scraped data into a dictionary or another structured format
        scraped_data = [{'title': title, 'url': url, 'content': ' '.join(content)}]

        # Debugging: print scraped content
        print(f"Scraped data from {url}:\n{scraped_data}\n")
        return scraped_data
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
