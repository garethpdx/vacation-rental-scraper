from scraper.parse import key_value


class PropertyScraper(object):
    def __init__(self, selectors):
        self.selectors = selectors

    def scrape(self, soup):
        property = {}
        for selector in self.selectors:
            property[selector] = self.selectors[selector].parse(soup)
        return property




class Selector(object):
    def __init__(self, redux_key):
        self.redux_key = redux_key

    def parse(self, redux):
        return key_value(redux, self.redux_key)


class TransformSelector(Selector):

    def __init__(self, redux_key, transformation):
        self.transformation = transformation
        super(TransformSelector, self).__init__(redux_key)

    def parse(self, redux):
        raw = super(TransformSelector, self).parse(redux)
        return self.transformation(raw)


