import json
import sys

import requests

from scraper.vendors import scraper_factory


if __name__ == '__main__':
    properties = []

    # read urls from stdin
    for url in sys.stdin:
        try:
            # if adding additional vendors, get vendor from URL or user
            scraper = scraper_factory(vendor='airbnb')
            response = requests.get(url.strip())
            html = response.text
            property = scraper.scrape(html)
            properties.append(property)
        except Exception as e:
            properties.append({"error": e,
                               "url": url[:80],
                               "msg": "Unable to scrape property listing."})
    print(json.dumps(properties))
