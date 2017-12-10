"""

Base objects used for scraping property data and selected elements
within said data.

PropertyScrapers take a list of extractors and a preprocessor, then apply
both to scraped content. To support additional vendors, it's likely
possible to simply write new selectors and a new preprocessor, but implementing
a new PropertyScraper is also an option when necessary.

Extractors use a selector to retrieve information from content by locating,
extracting, and optionally transforming it.

"""
from bs4 import BeautifulSoup


class HtmlPropertyScraper(object):
    " Extract selectors from a parsed property. "
    def __init__(self, extractors, preprocessor):
        self.extractors = extractors
        self.preprocessor = preprocessor

    def scrape(self, raw):
        " Fetch and parse html elements identified by selectors. "
        properties = {}
        parsed = self.parse(raw)
        for extractor in self.extractors:
            properties[extractor] = self.extractors[extractor].extract(parsed)
        return properties

    def parse(self, raw):
        soup = BeautifulSoup(raw, 'html.parser')
        return self.preprocessor(soup)


class TransformExtractor(object):
    " What and how to find, and what to do after finding "
    def __init__(self, selector, locate, transform=None, *args, **kwargs):
        self.selector = selector
        self.locate = locate
        if transform:
            self.transform = transform

    def extract(self, data):
        raw = self.locate(data, self.selector)
        return self.transform(raw)

    def transform(self, raw_value, *args, **kwargs):
        " Default transform just returns raw value "
        return raw_value


class ParseError(TypeError):
    " Failed to parse property content "
