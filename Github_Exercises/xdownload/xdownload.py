import bs4, requests, os

article_url = "http://www.vjenner.com/2016/05/vcap6-dcv-deployment-objective-1-1-perform-advanced-esxi-host-configuration/"
image_folder = "D:\VMware\VCAP\Objective 1.1"

article_res = requests.get(article_url)
article_res.raise_for_status()
article_soup = bs4.BeautifulSoup(article_res.text, "html.parser")

image_links = article_soup.select('a[class="grouped_elements"]')

if image_links == []:
    print("Cannot find image.")
    exit(1)
else:
    for links in image_links:
        image_url = links.get("href")
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        print("Downloading %s..." % image_url)
        image_file = open(os.path.join(image_folder, os.path.basename(image_url)), "wb")
        for image_chunk in image_res.iter_content(len(image_res.text)):
            image_file.write(image_chunk)
        image_file.close()
        
print("Done.")