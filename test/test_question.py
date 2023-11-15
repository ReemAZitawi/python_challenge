# test_strings.py
import pytest

from questions.mian import reverse_string, is_palindrome, remove_duplicates, list_sum, remove_element


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""


def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("python") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([]) == []



def test_list_sum():
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([-1, 0, 1]) == 0
    assert list_sum([]) == 0


def test_remove_element():
    # Test case 1
    assert remove_element([1, 2, 3, 4, 2, 5], 2) == [1, 3, 4, 5]

    # Test case 2
    assert remove_element(['apple', 'banana', 'orange', 'banana'], 'banana') == ['apple', 'orange']

    # Test case 3
    assert remove_element([], 42) == []

    # Test case 4
    assert remove_element([1, 2, 3], 4) == [1, 2, 3]