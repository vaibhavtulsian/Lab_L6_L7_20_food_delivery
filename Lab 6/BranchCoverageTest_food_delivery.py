import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# ============================================================================
# Branch & Edge Case Coverage Tests for delivery_charge
# ============================================================================

def test_delivery_charge_boundary_negative_distance():
    # Tests branch: distance_km <= 0 (negative)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(-1, 200, False)

def test_delivery_charge_boundary_zero_distance():
    # Tests branch: distance_km <= 0 (zero boundary)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_boundary_exceeds_max_distance():
    # Tests branch: distance_km > 15 (exceeds range)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(15.1, 200, False)

def test_delivery_charge_free_delivery_no_rain():
    # Tests branch: order_value >= 500 (True), is_raining (False)
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_free_delivery_with_rain():
    # Tests branch: order_value >= 500 (True), is_raining (True) -> 0 + 30 = 30
    assert delivery_charge(5, 550, True) == 30

def test_delivery_charge_short_distance_no_rain():
    # Tests branch: distance_km <= 3 (True), is_raining (False)
    assert delivery_charge(3, 499, False) == 20

def test_delivery_charge_short_distance_with_rain():
    # Tests branch: distance_km <= 3 (True), is_raining (True)
    assert delivery_charge(1.5, 200, True) == 50

def test_delivery_charge_medium_distance_no_rain():
    # Tests branch: 3 < distance_km <= 8 (True), is_raining (False)
    assert delivery_charge(8, 200, False) == 40

def test_delivery_charge_medium_distance_with_rain():
    # Tests branch: 3 < distance_km <= 8 (True), is_raining (True)
    assert delivery_charge(5, 200, True) == 70

def test_delivery_charge_long_distance_boundary_no_rain():
    # Tests branch: distance_km > 8 and <= 15 (True), is_raining (False)
    assert delivery_charge(15, 200, False) == 60

def test_delivery_charge_long_distance_with_rain():
    # Tests branch: distance_km > 8 and <= 15 (True), is_raining (True)
    assert delivery_charge(12, 100, True) == 90


# ============================================================================
# Branch & Edge Case Coverage Tests for apply_coupon
# ============================================================================

def test_apply_coupon_none_code():
    # Tests branch: code is None (True)
    assert apply_coupon(300, None, False) == 300

def test_apply_coupon_invalid_code():
    # Tests branch: code not in COUPONS (True)
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "DISCOUNT99", True)

def test_apply_coupon_welcome_not_first_order():
    # Tests branch: code == "WELCOME" and not is_first_order (True)
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_welcome_valid_first_order_eligible():
    # Tests branch: code == "WELCOME" and is_first_order (True), order_value >= 200 (True)
    assert apply_coupon(250, "WELCOME", True) == 150

def test_apply_coupon_welcome_valid_first_order_under_min_order():
    # Tests branch: code == "WELCOME" and is_first_order (True), order_value < 200 (True)
    assert apply_coupon(180, "WELCOME", True) == 180

def test_apply_coupon_save50_not_first_order_eligible():
    # Tests branch: code != "WELCOME", order_value >= 200 (True)
    assert apply_coupon(300, "SAVE50", False) == 250

def test_apply_coupon_save50_order_boundary_under_200():
    # Tests branch: code != "WELCOME", order_value < 200 (boundary 199)
    assert apply_coupon(199, "SAVE50", False) == 199

def test_apply_coupon_save50_order_boundary_exactly_200():
    # Tests branch: code != "WELCOME", order_value == 200 (eligible)
    assert apply_coupon(200, "SAVE50", True) == 150


# ============================================================================
# Branch & Edge Case Coverage Tests for estimated_time
# ============================================================================

def test_estimated_time_normal():
    # is_peak_hour=False, restaurant_busy=False -> 15 + 2*4 = 23
    assert estimated_time(2, False, False) == 23

def test_estimated_time_peak_only():
    # is_peak_hour=True, restaurant_busy=False -> 15 + 2*4 + 10 = 33
    assert estimated_time(2, True, False) == 33

def test_estimated_time_busy_only():
    # is_peak_hour=False, restaurant_busy=True -> 15 + 2*4 + 15 = 38
    assert estimated_time(2, False, True) == 38

def test_estimated_time_peak_and_busy():
    # is_peak_hour=True, restaurant_busy=True -> 15 + 2*4 + 10 + 15 + 5 = 53
    assert estimated_time(2, True, True) == 53
