import bs4, requests, os

os.makedirs("xkcd", exist_ok=True)
comic_url = "http://xkcd.com"

while not comic_url.endswith("#"):
    comic_res = requests.get(comic_url)
    comic_res.raise_for_status()
    comic_soup = bs4.BeautifulSoup(comic_res.text, "html.parser")

    comic_image = comic_soup.select("#comic img")
    if (comic_image == []):
        print("Could not find comic image.")
    else:
        image_url = "http:" + comic_image[0].get("src")
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        print("Downloading image %s..." % image_url)
        image_file = open(os.path.join("xkcd", os.path.basename(image_url)), "wb")
        for chunk in image_res.iter_content(len(image_res.text)):
            image_file.write(chunk)
        image_file.close()
        
    prev_image = comic_soup.select("a[rel='prev']")[0]
    comic_url = "http://xkcd.com" + prev_image.get("href")
        
print("Done.")