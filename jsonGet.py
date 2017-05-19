
def jsonGet(data, default, key1, *otherKeys):
    """function to extract values from a dict of dicts like what is returned
    by json.load"""
    
    if data is None:
        return default
        
    if key1 is None:
        return default
        
    if isinstance(data, dict):
        if key1 not in data:
            return default        
    elif isinstance(data, list):
        if len(data) == 0:
            return default
        if key1 < 0 or key1 >= len(data):
            return default
    else:
        return default
 
    data = data[key1]
    
    otherKeyCount = len(otherKeys)
    if otherKeyCount == 0:
        return data
        
    if not isinstance(data, dict) and not isinstance(data, list):
        return default
        
    for i, key in enumerate(otherKeys):
        if isinstance(data, dict):
            if key not in data:
                return default
        elif isinstance(data, list):
            if len(data) == 0:
                return default
            if key < 0 or key >= len(data):
                return default
        else:
            return default 
            
        data = data[key]
        
        # if this is the last key, we've found our data
        if i == otherKeyCount - 1:
            return data

    return default
            
