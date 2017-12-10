import json
import sys

import requests

from scraper.vendors import scraper_factory


if __name__ == '__main__':
    properties = []
    try:

        # read urls from stdin
        for url in sys.stdin:
            # TODO what if 2nd url explodes?
            response = requests.get(url.strip())
            html = response.text
            # if adding additional vendors, get vendor from URL or user
            scraper = scraper_factory(vendor='airbnb')
            property = scraper.scrape(html)
            properties.append(property)
        print(json.dumps(properties))
    except Exception as e:
        print json.dumps({"error": e,
                          "msg": "Unable to scrape property listing."})
