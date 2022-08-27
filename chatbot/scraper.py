import bs4
import requests

def google_search(query):
    url = 'https://google.com/search?q=' + "+".join(query.split())
    req = requests.get( url )
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    links = []
    for i, item in enumerate(soup.find_all( 'h3' )):
        if item.parent.get("href") is None: continue
        links.append({
            "title":item.getText(),
            "link":item.parent.get("href")[7:]
        })
    return links

def scholar_search(query):
    url = 'https://scholar.google.com.au/scholar?q=' + "+".join(query.split())
    req = requests.get( url )
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    links = []
    for i, item in enumerate(soup.find_all( 'h3' )):
        if item.a.get("href") is None: continue
        links.append({
            "title":item.getText(),
            "link":item.a.get("href")
        })
    return links

if __name__ == "__main__":
    q = input("Enter query: ")
    q = q.replace("search ", "")
    from pprint import pprint
    pprint(google_search(q))
    pprint(scholar_search(q))
