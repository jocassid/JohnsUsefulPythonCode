#!/usr/bin/env python3

# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from dirf import dirf


class Thingy:

    def foo_bar(self):
        pass

    def foo_Bar(self):
        pass


class TestDirf:

    def test_simple_contains(self):
        expected = ['lstrip', 'rstrip', 'strip']
        assert expected == dirf(dir('a'), 'strip')

    def test_case_sensitive_contains(self):
        expected = ['foo_bar']
        assert expected == dirf(dir(Thingy), 'bar', ignore_case=False)

    def test_startswith(self):
        expected = ['title', 'translate']
        assert expected == dirf(dir('a'), 't', starts_with=True)

