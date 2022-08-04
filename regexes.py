
from re import compile as re_compile
from re import IGNORECASE, VERBOSE


win_path_regex = re_compile(
    r"""
        ([a-z]+:\\)?            # drive A:\ etc
        (([\w\d\-_. ]+\\)+)?    # folders
        ([\w\d\-_. ]+)?         # file
    """,
    VERBOSE | IGNORECASE,
)

posix_path_regex = re_compile(
    r"""
        (/)?                    # root
        (([\w\d\-_. ]+/)+)?     # dirs
        ([\w\d\-_. ]+)?         # file
    """,
    VERBOSE | IGNORECASE,
)
