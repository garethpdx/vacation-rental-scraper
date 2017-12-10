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
    except AttributeError:
        # ignore values that don't quack like a dict
        pass
