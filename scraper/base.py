"""

"""
from bs4 import BeautifulSoup

from scraper.parse import nested_get


class PropertyScraper(object):

    def __init__(self, selectors, preprocessor):
        self.selectors = selectors
        self.preprocessor = preprocessor

    def scrape(self, html):
        " get content identified by selectors "
        soup = BeautifulSoup(html, 'html.parser')
        content = self.preprocessor(soup)
        properties = {}
        for selector in self.selectors:
            properties[selector] = self.selectors[selector].parse(content)
        return properties


class Selector(object):
    " Base class for parser selectors "

    def __init__(self, selector, transformation=None, *args, **kwargs):
        self.selector = selector
        if transformation:
            self.transformation = transformation

    def parse(self, data, *args, **kwargs):
        " fetch raw data at selector"
        raise NotImplementedError()

    def transformation(self, raw_value, *args, **kwargs):
        return raw_value


class TransformSelector(Selector):

    def parse(self, data):
        raw = nested_get(data, self.selector)
        return self.transformation(raw)


class ParseError(TypeError):
    " Failed to parse property content "
