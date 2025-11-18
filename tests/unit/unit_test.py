import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

@pytest.fixture
def custom_tax_rate():
    return 0.10 #this is different than default rate which is 0.07 in pricing.py

#Q3a - parse_price unit tests (given)
@pytest.mark.parametrize("string_input, expected_float_output", [
    ("$1,234.50", 1234.50),	#valid
    ("12.5", 12.5),		#valid
    ("$0.99", 0.99),		#valid
    ("abc", 0),			#invalid, should return 0
    ("$12,34,56",0)		#invalid, should return 0
])
def test_parse_price(string_input, expected_float_output):
    #the string inputted into parse_price should = expected_float
    assert parse_price(string_input) == expected_float_output

#Q3b - format_currency unit tests (rounding/format)
@pytest.mark.parametrize("float_input, formatted_string_output", [
    (0.9972, "$1.00"),		#rounding up
    (0.9912, "$0.99"), 		#rounding down
    (12.5, "$12.50"),		#format to 2 decimals
    (3, "$3.00"),		#format to 2 decimals
    (1234.50, "$1,234.50")	#format with thousand separator
])
def test_format_currency(float_input, formatted_string_output):
    #the value inputted into format_currency should = formatted_string_output
    assert format_currency(float_input) == formatted_string_output

#Q3c - apply_discount unit tests (0%, large %, negative raises)
def test_apply_discount_0():
    assert apply_discount(100, 0) == 100
def test_apply_discount_50():
    assert apply_discount(100, 50) == 50
def test_apply_discount_100():
    assert apply_discount(100, 100) == 0
def test_apply_discount_negative():
    assert apply_discount(100, -10) == 110

#Q3d - add_tax unit tests (default/custom, negative raises)
def test_add_tax_default():
    assert add_tax(100) == 107
def test_add_tax_custom(custom_tax_rate): #fixture usage here
    assert add_tax(100, custom_tax_rate) == 100 * (1 + custom_tax_rate)
def test_add_tax_negative():
    assert add_tax(100, -5) == 95

#Q3e - bulk_total unit tests (simple list)
def test_bulk_total():
    simple_list = [26, 7, 11, 6] #this total = 50, after default tax (0.07) should be 53.5 (no discount)
    assert bulk_total(simple_list) == 53.5
