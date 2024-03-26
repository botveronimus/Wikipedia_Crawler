from fetch_content import fetch_html
from parse_content import parse_main_content
from save_content import save_to_file

if __name__ == "__main__":
    URL = input("Article URL:")
    filename = input("File name:")

    # Fetch HTML
    html_content = fetch_html(URL)

    # Parse content
    main_content = parse_main_content(html_content)

    # Save content
    save_to_file(main_content, filename)
