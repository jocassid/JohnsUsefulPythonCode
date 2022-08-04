#!/usr/bin/env python3

# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from grouping import group, groupItem

def testGroupItem():

    assert ['a'] == groupItem('a', [], [])
    
    temp = groupItem('a', [], [])
    assert ['a','b'] == groupItem('b', [], temp)
    
    temp = {}
    for item in [('a', 0), ('a', 1), ('b', 2)]:
        temp = groupItem(item, [lambda x: x[0]], temp)
    #print('temp', temp)
    
    assert temp == {
        'a':[('a', 0), ('a', 1)], 
        'b':[('b', 2)]}

    items = [
        ('I','A',1),
        ('I','A',2),
        ('I','B',1),
        ('II','A',1),
        ('II','B',1)]
        
    expected = {
        'I':{
            'A':{
                1:[('I','A',1)],
                2:[('I','A',2)]},
            'B':{
                1:[('I','B',1)]}},
        'II':{
            'A':{
                1:[('II','A',1)]},
            'B':{
                1:[('II','B',1)]}}
    }
        
    actual = {}
    for item in items:
        actual = groupItem(
            item,
            [lambda x: x[0],
                lambda x: x[1],
                lambda x: x[2]],
            actual)

    assert actual == expected
    
            
            
def testGroup():
    
    items = [
        ('I','A',1),
        ('I','A',2),
        ('I','B',1),
        ('II','A',1),
        ('II','B',1)]
 
    expected = {
        'I':{
            'A':{
                1:[('I','A',1)],
                2:[('I','A',2)]},
            'B':{
                1:[('I','B',1)]}},
        'II':{
            'A':{
                1:[('II','A',1)]},
            'B':{
                1:[('II','B',1)]}}
    }
 
    actual = group(
        items,
        lambda i: i[0],
        lambda i: i[1],
        lambda i: i[2])
    
    assert actual == expected



