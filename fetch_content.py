import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def fetch_html(url: str) -> str:
    """Fetches HTML content of a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        logging.info(f"Successfully fetched content from {url}")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch content from {url}: {e}")
        raise
