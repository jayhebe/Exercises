import requests, sys, webbrowser, bs4

print("Baiduing...")

res = requests.get("http://www.baidu.com/s?wd=" + sys.argv[1])
res.raise_for_status()