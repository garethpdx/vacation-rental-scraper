"""

Airbnb uses redux, react[1], and hypernova[2] for content rendering

[1] https://github.com/airbnb/hypernova-react
[2] https://github.com/airbnb/hypernova

As a consequence, a copy of a property's details are available in a redux
script object.

The relevant script can be identified with a data attribute of 
hypernova-key=spaspabundlejs

The data is hidden within an html comment. Once uncommented, we have vanilla
JSON that can be converted into a dict

could go in a class

AirBNBPropertyScraper

but would still need a factory to choose the right class

"""

import json

from scraper.base import TransformSelector, Selector, ParseError

selectors = {
    'bedrooms': TransformSelector('bedroom_label',
                                  # 1 bedrooms
                                  lambda label: label.split(' ')[0]),
    'property_type': TransformSelector('room_type_category'),
    'amenities': TransformSelector('listing_amenities',
                                   lambda amenities: list(
                                       map(lambda amenity: amenity['name'],
                                           # if not is_present, then property doesn't have the feature
                                           # also, safety features aren't displayed in the list of amenities
                                           filter(lambda amenity: (amenity['is_present'] and
                                                                   not amenity['is_safety_feature']),
                                                  amenities))))}


def preprocessor(soup):
    """
    details of an Airbnb property are in a redux json object hidden
    within a comment
    """
    scripts = soup.findAll('script')
    for script in scripts:
        if is_repr(script):
            js = clean_repr(script.string)
            break
    else:
        raise ParseError("Could not parse. No hypernova properties found.")
    try:
        return json.loads(js)
    except json.JSONDecodeError as e:
        raise ParseError(e)


def is_repr(bs_script):
    """
    object representation is in string of hypernova script e.g.
    <script data-hypernova-key="spaspabundlejs">{object}</script>
    """
    # could be get() (like dict)
    return (bs_script.has_attr('data-hypernova-key') and
            bs_script.attrs['data-hypernova-key'] == 'spaspabundlejs')


def clean_repr(script_string):
    """
    "<!--{}-->" => "{}"
    """
    return script_string[4:-3]
