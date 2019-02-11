import requests  # Requests allows you to send organic, grass-fed HTTP/1.1 requests

'''
Python library for pulling data out of HTML and XML files.
It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree
'''
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 15

    while page <= max_pages:
        url = 'https://thenewboston.com//forum/category.php?id=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'title text-semibold'}):
            href = link.get('href')  # get all the links inside the 'a' tags that have the class 'title text-semibold'
            title = link.string  # get the text (title) in the 'a' tag
            title = title.strip()  # remove all the spaces at the beginning and end of the title
            print(title)
            print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    # if you want to gather information from that page
    for item_name in soup.findAll('span', {'class': 'date'}):
        print(item_name.string + '\n')
        # if you want to gather links for a web crawler
        # for link in soup.findAll('a'):
        #   href = "https://buckysroom.org" + link.get('href')
        #  print(href)


trade_spider(15)
