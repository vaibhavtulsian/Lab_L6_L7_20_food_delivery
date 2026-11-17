import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# Initial test cases
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

# Additional test cases to achieve 100% code (line) coverage
def test_delivery_charge_invalid_distance():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_free_delivery():
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_medium_distance():
    assert delivery_charge(5, 200, False) == 40

def test_delivery_charge_far_distance():
    assert delivery_charge(10, 200, False) == 60

def test_delivery_charge_with_rain():
    assert delivery_charge(2, 200, True) == 50

def test_apply_coupon_invalid_coupon():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID_CODE", False)

def test_apply_coupon_welcome_not_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_order_under_200():
    assert apply_coupon(150, "SAVE50", False) == 150

def test_apply_coupon_valid_save50():
    assert apply_coupon(300, "SAVE50", False) == 250

def test_estimated_time_standard():
    assert estimated_time(2, False, False) == 23

def test_estimated_time_peak_hour():
    assert estimated_time(2, True, False) == 33

def test_estimated_time_restaurant_busy():
    assert estimated_time(2, False, True) == 38

def test_estimated_time_busy_and_peak():
    assert estimated_time(2, True, True) == 53
