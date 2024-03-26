import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def save_to_file(content: str, file_path: str) -> None:
    """Saves content to a given file path."""
    file_path = file_path + ".txt"
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            logging.info(f"Content successfully saved to {file_path}")
    except IOError as e:
        logging.error(f"Failed to save content to {file_path}: {e}")
        raise

