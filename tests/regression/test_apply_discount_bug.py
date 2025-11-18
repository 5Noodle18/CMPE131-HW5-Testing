from src.pricing import apply_discount

def test_apply_discount():
    #apply_discount(price, discount) should multiply price * (100-discount)/100
    #in this case, 100 * (100-10)/100 ==> 100 * 90/100 ==> 100 * 0.9 ==> 90
    assert apply_discount(100.0, 10) == 90.0
