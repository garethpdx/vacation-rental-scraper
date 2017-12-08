import json
import sys

import requests

from scraper import scraper_factory, parse, selectors

def formatter(data):
    " "
    raw = json.dumps(data)

class Property(object):
    " worth having a class? "
    def __init__(self, bedrooms, prop_type, ameniies, **kwargs):
        # don't like the explitnes of this
        self.bedrooms = bedrooms
        self.type = prop_type
        self.ameniies = ameniies

    @classmethod
    def from_scrape(cls, scrape):
        # expect a scrape
        return cls.__init__(bedrooms=scrape.fetch('bedroom'),
                            prop_type=scrape.fetch('type'),
                            ameniies==scrape.fetch('ameniies'))

    def as_json(self):
        d = dict(bedrooms=bedrooms,
                 type=self.type,
                 ameniies=self.ameniies)
        return jsom.dumps(d)


if __name__ == '__main__':
    # this approach expects to read from stdin
    # a la curl $url | python airbnb_scraper

    # TODO validate urls?
    for url_in in sys.stdin:
        try:
            url = url_in.strip()
            data = requests.get(url)
        except requests.exceptions.RequestException as e:
            data = dict(error=e)

    soup = BeautifulSoup(t, 'html.parser')
    js = extract_redux(soup)
    props = listing_properties(js)
    print(json.dumps(props))
    
    scraper = scraper_factory('airbnb', html)
    property = Property.from_scrape(scraper)
