#!/usr/bin/env python3

def group(iterable, *keyFuncs):
    
    if len(keyFuncs) == 0:
        raise Exception(
            'there should be at least keyfunc argument')
    
    # Create the top-level dict
    output = {}
    for item in iterable:
        # At each call group item returns a modified version of the dict.
        # groupItem recursively applies the various key functions 
        output = groupItem(
            item,
            list(keyFuncs), 
            output)
    return output
    
def groupItem(item, keyFuncs, stuffIn):
    """group item takes an item and sorts it into a nested group of categories
    as defined by a list of key functions.  """
    
    # Are there any more key functions.  If not we've reached the bottom level
    # where we're adding items to a list.
    if len(keyFuncs) == 0:
        stuffIn.append(item)
        return stuffIn

    # There are still key functions to use.  Make sure that stuffIn is some
    # form of a dictionary
    if not issubclass(stuffIn.__class__, dict):
        raise Exception('keyFuncs is not empty stuffIn should be a dict')
        
    # Pop the first keyfunction from the list
    keyFunc = keyFuncs.pop(0)
    
    # Use the function to compute the value of the key
    key = keyFunc(item)
    
    # If there aren't any more key functions left after the pop operation
    if len(keyFuncs) == 0:
        if key in stuffIn.keys():
            stuffIn[key].append(item)
            return stuffIn
        stuffIn[key] = [item]
        return stuffIn
    
    if key in stuffIn.keys():
        stuffIn[key] = groupItem(item, keyFuncs, stuffIn[key])
        return stuffIn
    
    stuffIn[key] = groupItem(item, keyFuncs, {})
    return stuffIn
        

