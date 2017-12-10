"""

Airbnb uses redux, react[1], and hypernova[2] for content rendering.

As a consequence, a copy of a property's details are available in a redux
script object.

The relevant script can be found in a script with a data attribute of
hypernova-key=spaspabundlejs

The data is hidden within an html comment. Once uncommented, we have vanilla
JSON that can be converted into a dict

"""

import json

from scraper.base import TransformExtractor, ParseError
from scraper.parse import nested_get


def _is_amenity_present(amenity):
    return (
        # yes if is_present==True
        amenity['is_present'] and
        # safety features aren't visually rendered in the list of amenities,
        # so leave them out here too
        not amenity['is_safety_feature'])


def _amenity_name(amenity):
    return amenity['name']

selectors = {
    'bedrooms': TransformExtractor('bedroom_label',
                                   nested_get,
                                   #  e.g. bedroom_label: '1 bedrooms'
                                   lambda value: value.split(' ')[0]),
    'property_type': TransformExtractor('room_type_category', nested_get),
    'amenities': TransformExtractor('listing_amenities',
                                    nested_get,
                                    lambda amenities: [_amenity_name(amenity)
                                                       for amenity in amenities
                                                       if _is_amenity_present(amenity)])
}


def _is_repr(bs_script_tag):
    """
    Property representation is found in string of hypernova script e.g.
    <script data-hypernova-key="spaspabundlejs">{object}</script>
    """
    return bs_script_tag.get('data-hypernova-key') == 'spaspabundlejs'


def _clean_repr(script_string):
    """
    Property representation lives within an html comment

    "<!--{}-->" => "{}"
    """
    return script_string[4:-3]


def preprocessor(soup):
    """
    Preprocess an Airbnb scrape by finding the JSON representation
    and returning it. That way extractors can work with it as a dict.
    """
    scripts = soup.findAll('script')
    for script in scripts:
        if _is_repr(script):
            js = _clean_repr(script.string)
            break
    else:
        raise ParseError("Could not parse. No hypernova properties found.")
    try:
        return json.loads(js)
    except json.JSONDecodeError as e:
        raise ParseError(e)
