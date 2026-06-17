import pytest
from string_utils import StringUtils

string_utils = StringUtils()



@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("1abc", "1abc"),  
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("ABC", "Abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected




@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    (" python", "python"),
    ("no_spaces", "no_spaces"),  
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  
    ("   ", ""),  
    ("text   ", "text   "),  
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", True),
    ("Hello World", " ", True), 
    ("abc123", "1", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("Python", "z", False),
    ("", "a", False), 
    (" ", "-", False),  
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected




@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),  
    ("test123test", "test", "123"),  
    ("hello", "x", "hello"),  
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),  
    ("normal", "", "normal"),  
    ("same", "same", ""),  
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


 
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected" ,  [
    (" skypro" , "skypro"),
    ("   ", ""),
    ("   test", "test")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
  ("04 апреля 2023","04 апреля 2023"),
  ("",""),
  ("None", "None"),
  ("12345", "12345") 
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

