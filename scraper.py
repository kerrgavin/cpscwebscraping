import requests
import sys
import csv
from bs4 import BeautifulSoup

def get_labels(area):
    labels = []
    for label in area.find_all("th", class_="label"):
        labels.append(label.contents[0])
    return labels

def get_content(area):
    content = []
    for con in area.find_all("th", class_="content"):
        content.append(con.contents[0])
    return content

def get_pages(args, headers):
    pages = []
    for arg in args[1:]:
        pages.append(requests.get(arg, headers = headers))
    return pages

def get_soups(pages):
    soups = []
    for page in pages:
        soups.append(BeautifulSoup(page.text, 'html.parser'))
    return soups

def get_page_info(soups):
    info = []
    for soup in soups:
        info.append(soup.find(class_="info"))
    return info

def main():
    headers = {
    'User-Agent': 'Gavin Kerr',
    'From': 'kerr_gaivn@columbusstate.edu'
    }
    pages = get_pages(sys.argv, headers)
    soups = get_soups(pages)

    info = get_page_info(soups)
    labels = get_labels(info[0])
    content = []
    for part in info:
        content.append(get_content(part))

    with open("output.csv", mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(labels)
        for item in content:
            writer.writerow(item)

main()
