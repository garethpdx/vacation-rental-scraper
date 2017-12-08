from scraper.parse import key_value


class PropertyScraper(object):
    def __init__(self, selectors):
        self.selectors = selectors

    def scrape(self, soup):
        property = {}
        for selector in self.selectors:
            property[selector] = self.selectors[selector].parse(soup)
        return property


def scraper_factory(vendor):
    # TODO  might have a bad vendor name here
    return PropertyScraper(selectors[vendor])


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


# TODO - better lambda than x
# TODO - bedroom handle studio?

selectors = {'airbnb': {'bedrooms': TransformSelector('bedroom_label',
                                                      # 1 bedrooms
                                                      lambda x: x.split(' ')[0]),
                        'property_type': Selector('room_type_category'),
                        'ameniies': TransformSelector('listing_amenities',
                                                      lambda x: list(
                                                          map(lambda x: x['name'],
                                                              # if not is_present, then property doesn't have the feature
                                                              # also, safety features aren't displayed in the list of amenities
                                                              filter(lambda y: y['is_present'] and not y['is_safety_feature'],
                                                                     x))))}}
