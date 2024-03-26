from fetch_content import fetch_html
from save_content import save_to_file
url = input("Article link: ")
filename = input("File Name:") + "_html" + ".txt"
html_content = fetch_html(url)
save_to_file(html_content, filename)