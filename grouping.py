#!/usr/bin/env python3

def group(iterable, *keyFuncs):
    
    if len(keyFuncs) == 0:
        raise Exception(
            'there should be at least keyfunc argument')
    
    output = {}
    for item in iterable:
        output = groupItem(
            item,
            list(keyFuncs), 
            output)
    return output
    
def groupItem(item, keyFuncs, stuffIn):
    if len(keyFuncs) == 0:
        stuffIn.append(item)
        return stuffIn
        
    if not issubclass(stuffIn.__class__, dict):
        raise Exception('keyFuncs is not empty stuffIn should be a dict')
        
    keyFunc = keyFuncs.pop(0)
    key = keyFunc(item)
    
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
        

