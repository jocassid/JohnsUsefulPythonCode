
from re import subn


def normalize_whitespace(text_in):
    text_out, number_of_subs_made = subn(r'\s(\s)+', ' ', text_in)
    return text_out

