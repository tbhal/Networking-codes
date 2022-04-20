from urllib.request import urlopen, urljoin
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extarct_image_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\]', re.IGNORECASE)
    return img_regex.findall(page)

if __name__ == '_main__':
    target_url = 'http://youtube.com'
    site = download_page(target_url)
    image_locations = extarct_image_locations(site)
    for src in image_locations:
        print(urljoin(target_url, src))