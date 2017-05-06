import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
 
try:
    res.raise_for_status()
    f = open("pg1112.txt", "w", encoding="utf-8")
    f.write(res.text)
    f.close()
except Exception as err:
    print("There was a problem: %s" % (err))