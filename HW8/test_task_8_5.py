from task_8_5 import is_valid_parentheses


def test_valid_simple():
    assert is_valid_parentheses("()") is True


def test_valid_nested():
    assert is_valid_parentheses("(())") is True


def test_valid_multiple():
    assert is_valid_parentheses("()()") is True


def test_invalid_more_closing():
    assert is_valid_parentheses("())") is False


def test_invalid_more_opening():
    assert is_valid_parentheses("(()") is False


def test_invalid_order():
    assert is_valid_parentheses(")(") is False


def test_empty_string():
    assert is_valid_parentheses("") is True


def test_complex_valid():
    assert is_valid_parentheses("(()())") is True


def test_complex_invalid():
    assert is_valid_parentheses("(()))(") is False