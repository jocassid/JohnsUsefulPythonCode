# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another,
# party on dudes.

def jsonGet(data, default, first_key, *other_keys):
    """function to extract values from a dict of dicts like what is returned
    by json.load"""

    if data is None:
        return default

    if first_key is None:
        return default

    try:
        data = data[first_key]
    except (KeyError, IndexError):
        return default

    otherKeyCount = len(other_keys)
    if otherKeyCount == 0:
        return data

    for i, key in enumerate(other_keys):
        try:
            data = data[key]
        except (KeyError, IndexError):
            return default

        # if this is the last key, we've found our data
        if i == otherKeyCount - 1:
            return data

    return default
