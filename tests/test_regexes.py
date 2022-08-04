
from pytest import mark

from regexes import \
    posix_path_regex, \
    win_path_regex


class TestRegexes:

    @staticmethod
    def match_error(match):
        if not match:
            return "No match"
        return f"Only matched {match.group()}"

    @mark.parametrize(
        "test_input, expected_groups",
        (
            ('C:\\', ('C:\\', None, None, None)),
            ('AA:\\', ('AA:\\', None, None, None)),
            (
                r"C:\windows\foo.txt",
                ('C:\\', 'windows\\', 'windows\\', 'foo.txt')),
            (
                r'E:\Seagate Drive\vol5_2.3\data-foo_v2.4.dat',
                (
                    'E:\\',
                    'Seagate Drive\\vol5_2.3\\',
                    'vol5_2.3\\',
                    'data-foo_v2.4.dat',
                ),
            ),
            (
                r'src\core\main.java',
                (None, 'src\\core\\', 'core\\', 'main.java'),
            ),
            ('resume.docx', (None, None, None, 'resume.docx')),
        )
    )
    def test_win_path_regex(self, test_input, expected_groups):
        match = win_path_regex.fullmatch(test_input)
        assert match, self.match_error(match)
        assert match.group() == test_input
        assert match.groups() == expected_groups

    @mark.parametrize(
        "test_input, expected_groups",
        (
            ('/', ('/', None, None, None)),
            ('/opt/foo.txt', ('/', 'opt/', 'opt/', 'foo.txt')),
            (
                '/mnt/Seagate Drive/vol5_2.3/data-foo_v2.4.dat',
                (
                    '/',
                    'mnt/Seagate Drive/vol5_2.3/',
                    'vol5_2.3/',
                    'data-foo_v2.4.dat',
                ),
            ),
            (
                'src/core/main.java',
                (None, 'src/core/', 'core/', 'main.java'),
            ),
            ('resume.odt', (None, None, None, 'resume.odt')),
        ),
    )
    def test_posix_path_regex(self, test_input, expected_groups):
        match = posix_path_regex.fullmatch(test_input)
        assert match, self.match_error()
        assert match.group() == test_input
        assert match.groups() == expected_groups
