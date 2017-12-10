"""
New vendors must be registered here in the vendors dict
"""

from scraper.vendors.airbnb import selectors, preprocessor
from scraper.base import PropertyScraper


class UnrecognizedVendor(KeyError):
    " Vendor not recognized or supported "
    pass


def scraper_factory(vendor):
    try:
        return PropertyScraper(*vendors[vendor])
    except KeyError as e:
        raise UnrecognizedVendor(e)


#  register vendors
vendors = {'airbnb': (selectors, preprocessor)}
