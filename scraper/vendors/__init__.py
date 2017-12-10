" New vendors must be registered here in the vendors dict "

from scraper.vendors.airbnb import selectors, preprocessor
from scraper.base import HtmlPropertyScraper


class UnrecognizedVendor(KeyError):
    " Vendor not recognized or supported "
    pass


def scraper_factory(vendor):
    try:
        return HtmlPropertyScraper(*vendors[vendor])
    except KeyError as e:
        raise UnrecognizedVendor(e)


#  register vendors
vendors = {'airbnb': (selectors, preprocessor)}
