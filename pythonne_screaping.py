import requests
from bs4 import BeautifulSoup

# Function to fetch and parse the HTML content of a webpage
def get_page_content(url):
    
    response = requests.get(url)
    
    # If the request is successful (status code 200)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None

# Function to scrape article titles from a news website and display them in order
def scrape_article_titles(url):
    # Fetch the page content
    page_content = get_page_content(url)
    
    if page_content:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find all article titles on the webpage (assuming they are in <h2> tags)
        # You can modify the tag/class based on the structure of the webpage
        articles = soup.find_all('h2')

        # Display the titles in order
        if articles:
            print("Articles found:")
            for idx, article in enumerate(articles, start=1):
                print(f"{idx}. {article.text.strip()}")
        else:
            print("No articles found on the webpage.")

# URL of the website to scrape
url = 'https://www.python.org/blogs/'  # Replace this with the actual website URL

# Call the function to scrape and display article titles
scrape_article_titles(url)
