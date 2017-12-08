import json
import sys
import pprint

from bs4 import BeautifulSoup
import requests

from scraper.scraper import scraper_factory
from scraper.parse import extract_redux


if __name__ == '__main__':
    # this approach expects to read from stdin

    # TODO validate urls
    for url_in in sys.stdin:
        try:
            url = url_in.strip()
            data = requests.get(url).text
        except requests.exceptions.RequestException as e:
            data = dict(error=e)

    soup = BeautifulSoup(data, 'html.parser')
    js = extract_redux(soup)
    scraper = scraper_factory(vendor='airbnb')
    props = scraper.scrape(js)
    pprint.pprint(json.dumps(props))
