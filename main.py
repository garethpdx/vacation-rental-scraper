import json
import sys

from scraper import scraper_factory

def formatter(data):
    " "
    raw = json.dumps(data)

class Property(object):
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
    html = sys.stdin().read()
    scraper = scraper_factory('airbnb', html)
    property = Property.from_scrape(scraper)
