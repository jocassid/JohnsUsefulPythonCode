# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another,
# party on dudes.

def get_json(collection, default, first_key, *other_keys):
    """function to extract values from a dict of dicts like what is returned
    by json.load"""

    if first_key is None:
        return default

    keys = first_key, *other_keys

    for key in keys:
        try:
            collection = collection[key]
        except (KeyError, IndexError, TypeError):
            return default

    return collection

jsonGet = get_json
