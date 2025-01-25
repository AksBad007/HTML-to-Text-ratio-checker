import requests
from bs4 import BeautifulSoup

def calculate_html_to_text_ratio(html):
    soup = BeautifulSoup(html, 'html.parser')
    text_length = len(soup.get_text())
    html_length = len(str(soup))
    
    if html_length == 0:
        return 0
    
    ratio = text_length / html_length
    return ratio

if __name__ == "__main__":
    url = input("Enter URL: ")
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        ratio = calculate_html_to_text_ratio(html_content)
        print("HTML-to-Text Ratio:", ratio, "(", round(ratio * 100, 2) ,"%)")
    else:
        print("Failed to fetch HTML content. Status code:", response.status_code)
