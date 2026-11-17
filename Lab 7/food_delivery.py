import math
import re

def parse_order(items_csv):
    """
    Parses a comma-separated list of item:qty pairs into a dictionary.
    Hardened against None, empty strings, missing colons, non-integer values,
    and malformed inputs discovered during fuzz testing.
    """
    if not items_csv or not isinstance(items_csv, str):
        return {}
    order = {}
    for item in items_csv.split(','):
        item = item.strip()
        if not item or ':' not in item:
            continue
        parts = item.split(':')
        if len(parts) != 2:
            continue
        name, qty_str = parts[0].strip(), parts[1].strip()
        if not name:
            continue
        try:
            qty = int(qty_str)
            if qty > 0:
                order[name] = qty
        except (ValueError, TypeError):
            continue
    return order

def delivery_eta(distance_km):
    """
    Calculates delivery ETA in minutes.
    Hardened against None, empty strings, non-numeric values, negative distances,
    NaN, and Infinity. Returns safe default base ETA (15) on invalid input.
    """
    if distance_km is None:
        return 15
    try:
        dist = float(distance_km)
        if math.isnan(dist) or math.isinf(dist) or dist < 0:
            return 15
        return int(15 + dist * 4)
    except (ValueError, TypeError, OverflowError):
        return 15

def coupon_discount(code):
    """
    Extracts discount value from coupon code (e.g., 'SAVE50' -> 50).
    Hardened against None, empty strings, missing 'SAVE', non-numeric suffixes,
    and malformed strings. Returns 0 on invalid or non-matching coupons.
    """
    if not code or not isinstance(code, str):
        return 0
    clean = code.strip().upper()
    if 'SAVE' not in clean:
        return 0
    parts = clean.split('SAVE')
    if len(parts) < 2 or not parts[1]:
        return 0
    digits = re.match(r'^\d+', parts[1])
    if digits:
        try:
            return int(digits.group())
        except (ValueError, OverflowError):
            return 0
    return 0

def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)

if __name__ == "__main__":
    main()
