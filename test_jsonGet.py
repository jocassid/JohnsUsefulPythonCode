
# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from jsonGet import jsonGet

def testJsonGet():
    assert jsonGet(None, 'default', None) == 'default'
    assert jsonGet({'a':'alpha'}, 'default', None) == 'default'
    
    # Miss on 1st level of 1 level dictionary
    assert jsonGet({'a':'alpha'}, None, 'b') is None
    
    # Hit on 1st level of 1 level dictionary
    assert jsonGet({'a':'alpha'}, None, 'a') == 'alpha'
    
    I_B = {
        1:'I-B-1',
        2:'I-B-2'
    }
    
    I = {
        'A':{
            1:'I-A-1',
            2:'I-A-2'
        },
        'B':I_B
    }
    
    jsonData = {
        'I':I,
        'II':{
            'A':{
                1:'II-A-1',
                2:'II-A-2'
            },
            'B':{
                1:'II-B-1',
                2:'II-B-2'
            }            
        }
    }
    
    # Miss on 1st level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'III') == 42
    
    # Hit on 1st level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'I') == I
    
    # Miss on 2nd level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'I', 'C') == 42
    
    # Hit on 2nd level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'I', 'B') == I_B

    # Miss on 3rd level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'I', 'A', 3) == 42

    # Hit on 3rd level of multi-level dictionary
    assert jsonGet(jsonData, 42, 'I', 'A', 1) == 'I-A-1'
    
    # data is not dictionary
    assert jsonGet('something', 42, 'I') == 42
    
    # 2nd level is not dictionary
    assert jsonGet({'I':'foo'}, 42, 'I', 'A') == 42
    
    # 3rd level is not dictionary
    assert jsonGet({'I':{'A':'foo'}}, 42, 'I', 'A', 1) == 42
    

def testJsonGetWithLists():
    
    # Top level is list
    assert jsonGet([], 42, 0) == 42
    
    # index outside of list bounds
    assert jsonGet([2, 2], 42, 2) == 42
    
    # 2nd level is list
    assert jsonGet({'foo':[2,4,9]}, 42, 'foo', 1) == 4 
    
    # 3 levels of lists
    data = [
        [
            [1, 1, 2, 3, 5],
            [1, 1, 4, 9, 25]
        ],
        [
            [2, 3, 5, 7],
            [4, 6, 10, 14],
            [6, 9, 15, 21]
        ],
    ]
    assert jsonGet(data, 42, 1, 2, 3) == 21

