import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def post_process_content(text: str) -> str:
    """
    Removes specific sections from the extracted text.

    Args:
    - text: The full text content from which to remove sections.

    Returns:
    - The cleaned text with specified sections removed.
    """
    # Regular expressions to identify sections to remove
    # Adjust these patterns based on the actual text structure
    patterns_to_remove = [
        r'\nSee also\[edit\].*?(?=\n[^\n]+?\[edit\]|\Z)',  # 'See also' section
        r'\nReferences\[edit\].*?(?=\n[^\n]+?\[edit\]|\Z)',  # 'References' section
        r'\nExternal links\[edit\].*?(?=\n[^\n]+?\[edit\]|\Z)',  # 'External links' section
        r'Not to be confused with.*\n',  # Disambiguation notice
        # Add more patterns as needed
    ]

    # Remove identified sections
    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text, flags=re.DOTALL)

    logging.info("Content has been post-processed to remove unwanted sections.")
    return text
