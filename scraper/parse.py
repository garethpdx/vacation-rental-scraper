" Tools for nested dictionaries of unknown structure "


def nested_get(nested_dict, needle):
    """
    recursively search nested dictionaries for key 'needle' and return value
    """
    try:
        for k, v in nested_dict.items():
            if k == needle:
                return v
            value = nested_get(v, needle)
            if value is not None:
                return value
    except AttributeError:
        # ignore values that don't quack like a dict
        pass


def key_path(nested_dict, needle, path=None):
    """
    recursively search nested dictionaries for a key named 'needle',
    returning path to the key as a list
    """
    if path is None:
        path = []
    try:
        for k, v in nested_dict.items():
            if k == needle:
                path.insert(0, k)
                return path
            location = key_path(nested_dict[k], needle, path)
            if location:
                location.insert(0, k)
                return path
    except AttributeError:
        # ignore values that don't quack like a dict
        pass
