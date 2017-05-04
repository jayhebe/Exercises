import webbrowser, requests, sys, bs4

print("Googling...")

if (len(sys.argv) > 1):
    keywords = " ".join(sys.argv[1:])
    googleRes = requests.get("http://www.google.com/search?q=" + keywords)
    googleRes.raise_for_status()
    
    googleSoup = bs4.BeautifulSoup(googleRes.text, "html.parser")
    googleElems = googleSoup.select(".r a")
    
    numOpen = min(5, len(googleElems))
    for i in range(numOpen):
        webbrowser.open("http://www.google.com/" + googleElems[i].get("href"))