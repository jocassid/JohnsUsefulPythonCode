

def first_true(iterable):
    for item in iterable:
        if item:
            return item
    return None


def first_is_not_none(iterable):
    for item in iterable:
        if item is not None:
            return item
    return None




