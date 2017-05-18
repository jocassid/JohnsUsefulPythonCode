
from ..noneValue import noneValue

def testNoneValue():
    assert noneValue(5, 3) == 5
    assert noneValue(None, 3) == 3
    assert noneValue(5, 3, 2) == 2
    assert noneValue(None, 3, 2) == 2


