import urllib.request
from bs4 import BeautifulSoup
from queue import *

root_url = "given_url"


def is_same_domain(url):
    if root_url in url:
        return True
    return False


def sanitize_url(url):
    if '#' in url:
        return url[0:url.find("#")]
    elif '?' in url:
        return url[0:url.find("?")]
    if url[-1] == '/':
        return url[:-1]
    return url


def get_all_a_tags(url):
    response = urllib.request.urlopen(root_url)
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    anchor_tags = soup.select("a")
    return [sanitize_url(a.get("href")) for a in anchor_tags]


queue = Queue()
queue.put(root_url)

url_list = []

while not queue.empty():
    current_url = queue.get()
    a_tags = get_all_a_tags(current_url)
    for link in a_tags:
        if is_same_domain(link) and link not in url_list:
            url_list.append(link)
            queue.put(link)

print(url_list)
