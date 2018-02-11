# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another,
# party on dudes.

def jsonGet(data, default, first_key, *otherKeys):
    """function to extract values from a dict of dicts like what is returned
    by json.load"""

    if data is None:
        return default

    if first_key is None:
        return default

    if isinstance(data, dict):
        if first_key not in data:
            return default
    elif isinstance(data, list):
        if not (0 <= first_key < len(data)):
            return default
    else:
        return default

    data = data[first_key]

    otherKeyCount = len(otherKeys)
    if otherKeyCount == 0:
        return data

    for i, key in enumerate(otherKeys):
        if isinstance(data, dict):
            if key not in data:
                return default
        elif isinstance(data, list):
            if not (0 <= key < len(data)):
                return default
        else:
            return default

        data = data[key]

        # if this is the last key, we've found our data
        if i == otherKeyCount - 1:
            return data

    return default
