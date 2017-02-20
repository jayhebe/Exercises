import requests, bs4

# res = requests.get("http://www.baidu.com")
# res.raise_for_status()
# baidu = bs4.BeautifulSoup(res.text, "html.parser")
# print(baidu.select("div"))

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
# print(type(exampleSoup))
print(exampleSoup.select("p"))