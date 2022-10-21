#!/usr/bin/env python3

# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

def group(iterable, *keyFuncs):
    
    if not keyFuncs:
        raise Exception(
            'there should be at least one keyfunc argument')
    
    # Create the top-level dict
    output = {}
    for item in iterable:
        # At each call group item returns a modified version of the dict.
        # groupItem recursively applies the various key functions 
        output = groupItem(item, keyFuncs, output)
    return output


def groupItem(item, key_funcs, stuffIn):
    """group item takes an item and sorts it into a nested group of categories
    as defined by a list of key functions."""
    key_funcs = list(key_funcs)
    
    # Are there any more key functions.  If not we've reached the bottom level
    # where we're adding items to a list.
    if not key_funcs:
        stuffIn.append(item)
        return stuffIn

    # There are still key functions to use.  Make sure that stuffIn is some
    # form of a dictionary
    if not issubclass(stuffIn.__class__, dict):
        raise Exception('keyFuncs is not empty stuffIn should be a dict')
        
    keyFunc, *key_funcs = key_funcs
    
    # Use the function to compute the value of the key
    key = keyFunc(item)
    
    # If there aren't any more key functions left after the pop operation
    if not key_funcs:
        if not key in stuffIn:
            stuffIn[key] = []
        stuffIn[key].append(item)
        return stuffIn
    
    stuffIn[key] = groupItem(item, key_funcs, stuffIn.get(key, {}))

    return stuffIn

  
