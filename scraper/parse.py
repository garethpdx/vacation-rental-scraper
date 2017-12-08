"""

"""

import json, pprint, codecs
from bs4 import BeautifulSoup


def traverse_dict(d, depth=0):
    depth += 1
    for key in d:
        dcts = []
        if isinstance(d[key], dict):
            dcts.append(key)
        else:
            print ('{0}{1}'.format('-'*depth,key))
        for child_key in dcts:
            print ('{0}{1}'.format('-'*depth,child_key))
            traverse_dict(d[child_key], depth)


def key_path(d, needle, path=None):
    if path is None:
        path = []
    for key in d:
        if key == needle:
            path.insert(0, key)
            return path
        if isinstance(d[key], dict):
            location =  key_path(d[key], needle, path)
            if location:
                location.insert(0, key)
                return path


def key_value(d, needle):
    path = key_path(d, needle)
    for key in path:
        d = d.get(key)
    return d

def extract_redux(soup):
    scripts = soup.findAll('script')
    
    for script in scripts:
        if script.has_attr('data-hypernova-key') and script.attrs['data-hypernova-key'] == 'spaspabundlejs':
            commented_js = script.string
    
    return json.loads(commented_js[4:-3])

def listing_properties(redux):

    amenities = map(lambda x: x['name'],
                    # if not is_present, then property doesn't have the feature
                    # also, safety features aren't displayed in the list of amenities
                    filter(lambda y: y['is_present'] and not y['is_safety_feature'],
                           key_value(js, 'listing_amenities')))

    return dict(property_id=property_id,
                bedrooms=key_value(js, 'bedroom_label').split(' ')[0],
                type=key_value(js, 'room_type_category'),
                amenities=list(amenities))
    

if __name__ == '__main__':
    t = ''
    property_id = '19292873'
    with codecs.open(property_id, encoding='utf-8') as f:
        t = f.read()
    soup = BeautifulSoup(t, 'html.parser')
    js = extract_redux(soup)
    props = listing_properties(js)
    print(json.dumps(props))
