
def room_type(html):
    types = ['Studio',]

class PropertyScraper(object):
    def __init__(self):
        self.selectors = [
            {'name': 'property_type',
             'selector': 'div a',
             'extractor': lambda x: x.split()[1]
            },
            {'name': 'bedrooms',
             'selector': 'bla',
            }
        ]

    def fetch(self, name):
        filter(lambda x: x['name'], self.selectors)

class AirBNBScraper(PropertyScraper):
    def __init__(self):
        self.


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

# 
# 
# parse amenities html               


class RegexpSelector(object):
    def fetch(self, content):
        """
        """
        import re
        return re.search(self.pattern, content)
    
    

class TagSelector(object):
    pass

class TypeSelector(RegexpSelector):
    def __init__(self):
        self.pattern = 'room_label":"\w+"'

class BedroomSelector(object):
    def __init__(self):
        self.pattern = 'bed_label":"\d bed"'
