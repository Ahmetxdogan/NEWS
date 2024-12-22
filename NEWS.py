import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

target_url = "https://news.ycombinator.com/"

#sayaç
counter = -1

found_links = set() #benzersizlikler için set kullanılır.

response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")



for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        parsed_uri = urlparse(href)
        if parsed_uri.scheme == 'https':
            found_links.add(href)
            counter += 1
            print(f"{counter}. Link: {href}")
            if counter == 10:
                print("yeterli linke ulaşıldı")
                break
                if counter < 10:
                    print("10 adet link yok")







