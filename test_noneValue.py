
# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from noneValue import noneValue

def testNoneValue():
    assert noneValue(5, 3) == 5
    assert noneValue(None, 3) == 3
    assert noneValue(5, 3, 2) == 2
    assert noneValue(None, 3, 2) == 3


