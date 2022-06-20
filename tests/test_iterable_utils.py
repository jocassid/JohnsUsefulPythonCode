
from iterable_utils import \
    first_is_not_none, \
    first_true


def test_first_true():
    assert first_true([0, [], 'foo', False, 'bar']) == 'foo'
    assert first_true([0, [], '']) is None
    assert first_true([]) is None


def test_first_is_not_none():
    assert first_is_not_none([None, 0, None, False]) == 0
    assert first_is_not_none([None, None]) is None
    assert first_is_not_none([]) is None







