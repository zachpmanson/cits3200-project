import bs4
import requests

def google_search(query):
    url = 'https://google.com/search?q=' + query
    req = requests.get( url )
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    print(soup)
    results = soup.find_all( 'h3' )
    for item in results:
        print(item.getText())
