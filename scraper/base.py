"""

"""
from bs4 import BeautifulSoup

from scraper.parse import nested_get



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
