from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def parse_main_content(html_content: str) -> str:
    """Parses the main content from the HTML, excluding unnecessary parts."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Focus on the main content area of Wikipedia articles
    main_content = soup.find(id="mw-content-text").get_text()

    # Further cleaning can be done here

    logging.info("Successfully parsed the main content.")
    return main_content
