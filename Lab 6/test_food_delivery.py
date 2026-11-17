import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# ============================================================================
# Starter test cases
# ============================================================================

def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

# ============================================================================
# Comprehensive Test Suite (100% Code & Branch Coverage)
# ============================================================================

def test_delivery_charge_boundary_negative():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(-1, 200, False)

def test_delivery_charge_boundary_zero():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_boundary_exceeds_max():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(15.1, 200, False)

def test_delivery_charge_free_delivery_no_rain():
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_free_delivery_with_rain():
    assert delivery_charge(5, 500, True) == 30

def test_delivery_charge_tier_1_with_rain():
    assert delivery_charge(3, 200, True) == 50

def test_delivery_charge_tier_2_no_rain():
    assert delivery_charge(8, 200, False) == 40

def test_delivery_charge_tier_2_with_rain():
    assert delivery_charge(5, 200, True) == 70

def test_delivery_charge_tier_3_no_rain():
    assert delivery_charge(15, 200, False) == 60

def test_delivery_charge_tier_3_with_rain():
    assert delivery_charge(10, 200, True) == 90

def test_apply_coupon_invalid():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", False)

def test_apply_coupon_welcome_not_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_welcome_first_order_eligible():
    assert apply_coupon(250, "WELCOME", True) == 150

def test_apply_coupon_welcome_first_order_under_200():
    assert apply_coupon(150, "WELCOME", True) == 150

def test_apply_coupon_save50_eligible():
    assert apply_coupon(300, "SAVE50", False) == 250

def test_apply_coupon_save50_under_200():
    assert apply_coupon(180, "SAVE50", False) == 180

def test_estimated_time_standard():
    assert estimated_time(2, False, False) == 23

def test_estimated_time_peak_only():
    assert estimated_time(2, True, False) == 33

def test_estimated_time_busy_only():
    assert estimated_time(2, False, True) == 38

def test_estimated_time_peak_and_busy():
    assert estimated_time(2, True, True) == 53
