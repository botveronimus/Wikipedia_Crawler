import requests
from save_content import save_to_file
def get_wikipedia_content(url):
    """
    Fetches plain text content of a Wikipedia page given its URL.

    Parameters:
    - url (str): The URL of the Wikipedia page.

    Returns:
    - str: The plain text content of the Wikipedia page.
    """
    # Extract the title of the page from the URL
    title = url.split('/')[-1]

    # Wikipedia API endpoint for fetching page content
    api_url = f"https://en.wikipedia.org/w/api.php"

    # Parameters for the API request
    params = {
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'extracts',
        'explaintext': True,
    }

    # Make the request to the Wikipedia API
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extract the page content from the response
    page = next(iter(data['query']['pages'].values()))
    content = page.get('extract', 'Content not found.')

    return content

# Example URL of a Wikipedia page
url = input("Article Link:")
filename = input("File name:")
content = get_wikipedia_content(url)
save_to_file(content, filename)

