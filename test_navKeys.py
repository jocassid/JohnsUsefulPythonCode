
from ..navKeys import navKeys

def testNavKeys():
    assert navKeys({'a':'alpha'}, None, 'b') is None
    assert navKeys({'a':'alpha'}, None, 'a') == 'alpha'
    
    jsonData = {
        'I':{
            'A':{
                1:'I-A-1',
                2:'I-A-2'
            },
            'B':{
                1:'I-B-1',
                2:'I-B-2'
            }
        },
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
    
    assert navKeys(jsonData, 42, 'III') == 42

