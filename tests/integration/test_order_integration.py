import pytest
from src.order_io import load_order, write_receipt

def no_discount():
    return 0
def cheap_discount():
    return 10
def BOGO_discount():
    return 50

def no_tax_rate():
    return 0.00
def standard_tax_rate():
    return 0.10
def high_tax_rate():
    return 0.20

def test_order_integration_default(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget, $10.00\ngizmo, 5.50\n", encoding="utf-8")

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent = 10, tax_rate = 0.1)

    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL:" in output_text

@pytest.mark.parametrize("order, assertions, discount, rate", [
    (   #since no discount or tax-rate, no change should occur
        "widget, $10.00\ngizmo, 5.50\n",
        ["widget: $10.00", "gizmo: $5.50", "TOTAL:"],
        no_discount(),
        no_tax_rate()
    ),
    (	#this should be exactly like the default
        "widget, $10.00\ngizmo, 5.50\n",
        ["widget: $10.00", "gizmo: $5.50", "TOTAL:"],
        cheap_discount(),
        standard_tax_rate()
    ),
    (	#half off prices (* 0.5), no extra tax -- this FAILS b/c of how write_receipt prints lines not using discounted values/rate
        "widget, $10.00\ngizmo, 5.50\n",
        ["widget: $5.00", "gizmo: $2.75", "TOTAL:"],
        BOGO_discount(),
        no_tax_rate()
    ),
    (   #half off prices (* 0.5), high tax (* 1.2) -- this FAILS b/c of how write_receipt prints lines not using discounted values/rate
        "widget, $10.00\ngizmo, 5.50\n",
        ["widget: $6.00", "gizmo: $3.30", "TOTAL:"],
        BOGO_discount(),
        high_tax_rate()
    ),
])
def test_order_integration_parametrized(tmp_path, order, assertions, discount, rate):
    input_file = tmp_path / "order.csv"
    input_file.write_text(order)

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount, rate)

    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    for assertion in assertions:
        assert assertion in output_text
