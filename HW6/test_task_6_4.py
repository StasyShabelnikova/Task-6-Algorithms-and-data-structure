from task_6_4 import longest_palindrome


def test_empty():
    assert longest_palindrome("") == ""


def test_one_char():
    assert longest_palindrome("a") == "a"


def test_odd_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]


def test_even_palindrome():
    assert longest_palindrome("cbbd") == "bb"


def test_full_string():
    assert longest_palindrome("racecar") == "racecar"


def test_no_long_palindrome():
    assert longest_palindrome("abc") in ["a", "b", "c"]


def test_longer_case():
    assert longest_palindrome("abacdfgdcaba") in ["aba"]


def test_even_full():
    assert longest_palindrome("abba") == "abba"