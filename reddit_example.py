import requests
import sys
import csv
from bs4 import BeautifulSoup

def main():
    filename = sys.argv[1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }

    search_page = requests.get("https://www.reddit.com", headers=headers)

    search_soup = BeautifulSoup(search_page.text.encode("utf-8"), "html.parser")

    promoted = search_soup.find_all(class_="promotedlink")
    for p in promoted:
        p.decompose()

    posts = search_soup.find_all(class_="Post")

    header = ["Subreddit", "Poster", "Link", "Comments"]

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for post in posts:
            post_info = []
            post_info.append(post.find("a", {"data-click-id":"subreddit"}).get("href"))
            post_info.append(post.find(class_ = "_2tbHP6ZydRpjI44J3syuqC").get("href"))
            post_info.append(post.find("a", {"data-click-id":"timestamp"}).get("href"))
            post_info.append(post.find("a", {"data-click-id":"comments"}).find("span").contents[0])
            writer.writerow(post_info)
main()
