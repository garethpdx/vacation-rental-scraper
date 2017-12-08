
def room_type(html):
    types = ['Studio',]

class PropertyScraper(object):
    def __init__(self, selectors):
        self.selectors = selectors

    def fetch(self, name):
        filter(lambda x: x['name'], self.selectors)



# alternative mebbe passing selectors to propertyscraper w/a factory, not having a airbnbscraper subclass

selectors = {
    'airbnb':
    {'name': 'property_type',
     'selector': 'div a',
     'extractor': lambda x: x.split()[1]
    },
    {'name': 'bedrooms',
     'selector': 'bla',
    }
}

def scraper_factory(self, vendor='airbnb'):
    # TODO  might have a bad vendor name here
    scraper = PropertyScraper(selectors[vendor])


# parse amenities html               


from parse import key_path, key_value

class Selector(object):
    def __init__(redux_key):
        self.redux_key = redux_key

class NakedSelector(Selector):

    def parse(self, redux):
        return key_value(redux, self.redux_key)

class TransformSelector(Selector):

    def __init__(self, redux_key, transformation):
        self.redux_key = redux_key
        self.transformation = transformation

    def parse(self, redux):
        raw = key_value(redux, self.redux_key)
        return transformation(raw)


# TODO - better lambda than x
# TODO - bedroom handle studio?

selectors = {'bedrooms': TransformSelector('bedroom_label',
                                           # 1 bedrooms
                                           lambda x: x.split(' ')[0])
             'property_type': NakedSelector('room_type_category'),
             'ameniies': TransformSelector('listing_amenities',
                                           lambda x: list(
                                               map(lambda x: x['name'],
                                                   # if not is_present, then property doesn't have the feature
                                                   # also, safety features aren't displayed in the list of amenities
                                                   filter(lambda y: y['is_present'] and not y['is_safety_feature'],
                                                          x))

