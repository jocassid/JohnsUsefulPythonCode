
# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.


def noneValue(test, valueIfNone, valueIfNotNone=None):
    if test is None:
        return valueIfNone
    if valueIfNotNone is None:
        return test
    return valueIfNotNone



