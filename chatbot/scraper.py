import bs4
import requests

def google_search(query):
    url = 'https://google.com/search?q=' + query
    req = requests.get( url )
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    returnVal = ""
    for i, item in enumerate(soup.find_all( 'h3' )):
        if item.parent.get("href") is None: continue
        print(i, item.getText())
        print(item.parent.get("href")[7:])
        returnVal += item.getText() + "\n"
        returnVal += item.parent.get("href")[7:] + "\n"
    return returnVal

if __name__ == "__main__":
    q = input()
    q = q.replace("search ", "")
    google_search(q)
