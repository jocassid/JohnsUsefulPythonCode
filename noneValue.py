
def noneValue(test, valueIfNone, valueIfNotNone=None):
    if test is None:
        return valueIfNone
    if valueIfNotNone is None:
        return test
    return valueIfNotNone



