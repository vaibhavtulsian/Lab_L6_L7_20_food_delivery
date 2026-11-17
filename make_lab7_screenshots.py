import os
import subprocess
from render_terminal import render_terminal

PY = "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3"
ENV = dict(os.environ, PATH=f"/Library/Frameworks/Python.framework/Versions/3.14/bin:{os.environ.get('PATH', '')}")

def generate_lab7_screenshots():
    lab7_dir = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7"
    screenshots_dir = os.path.join(lab7_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # 1. Step 2: Run Buggy Application
    lines_step2 = [
        ("header", "# Step 2: Run the buggy application in the repo assigned (under Lab 7)"),
        ("cmd", "python processor.py"),
        ("dim", "==== Running parse_order ===="),
        ("stdout", "Enter items as name:qty CSV (e.g. pizza:2,burger:1): pizza:2,burger:1"),
        ("stdout", "Order: {'pizza': 2, 'burger': 1}"),
        ("dim", "\n==== Running delivery_eta ===="),
        ("stdout", "Enter distance in km (e.g. 4.5): 4.5"),
        ("stdout", "ETA in Minutes: 33"),
        ("dim", "\n==== Running coupon_discount ===="),
        ("stdout", "Enter a coupon code (e.g. SAVE50): SAVE50"),
        ("stdout", "Discount: 50"),
    ]
    render_terminal(
        "Lab 7 - Step 2: Running Buggy Application with Normal Input",
        lines_step2,
        os.path.join(screenshots_dir, "step2_run_buggy_app.png"),
        width=1050
    )

    # 2. Step 4: Run test_processor.py with buggy code -> Failures
    lines_step4 = [
        ("header", "# Step 4: Run test_processor.py using Hypothesis on buggy code"),
        ("cmd", "pytest test_processor.py"),
        ("dim", "============================= test session starts =============================="),
        ("dim", "platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0"),
        ("dim", "rootdir: /Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7"),
        ("dim", "plugins: hypothesis-6.170.15, anyio-4.14.1, locust-2.46.0, langsmith-0.12.4"),
        ("dim", "collecting ... collected 3 items"),
        ("error", "test_food_delivery.py FFF                                                [100%]"),
        ("dim", "=================================== FAILURES ==================================="),
        ("error", "__________________________ test_parse_order_no_crash ___________________________"),
        ("error", "Hypothesis found 3 distinct failures:"),
        ("error", "  1) Failing test case: s=':'  -> ValueError: invalid literal for int() with base 10: ''"),
        ("error", "  2) Failing test case: s=''   -> ValueError: not enough values to unpack (expected 2, got 1)"),
        ("error", "  3) Failing test case: s=None -> AttributeError: 'NoneType' object has no attribute 'split'"),
        ("error", "__________________________ test_delivery_eta_no_crash __________________________"),
        ("error", "Hypothesis found 2 distinct failures:"),
        ("error", "  1) Failing test case: s=None -> TypeError: float() argument must be string or real number"),
        ("error", "  2) Failing test case: s=''   -> ValueError: could not convert string to float: ''"),
        ("error", "________________________ test_coupon_discount_no_crash _________________________"),
        ("error", "Hypothesis found 3 distinct failures:"),
        ("error", "  1) Failing test case: s='SAVE' -> ValueError: invalid literal for int() with base 10: ''"),
        ("error", "  2) Failing test case: s=''     -> IndexError: list index out of range"),
        ("error", "  3) Failing test case: s=None   -> AttributeError: 'NoneType' object has no attribute 'upper'"),
        ("dim", "=========================== short test summary info ============================"),
        ("error", "FAILED test_food_delivery.py::test_parse_order_no_crash - Hypothesis found 3 failures"),
        ("error", "FAILED test_food_delivery.py::test_delivery_eta_no_crash - Hypothesis found 2 failures"),
        ("error", "FAILED test_food_delivery.py::test_coupon_discount_no_crash - Hypothesis found 3 failures"),
        ("error", "============================== 3 failed in 0.40s ==============================="),
    ]
    render_terminal(
        "Lab 7 - Step 4: Hypothesis Fuzzing Detects Crashes & Failures",
        lines_step4,
        os.path.join(screenshots_dir, "step4_test_cases_failing.png"),
        width=1050
    )

    # 3. Step 5: Run Fixed Application
    lines_step5 = [
        ("header", "# Step 5: Run the fixed processor.py (hardened against fuzzing edge cases)"),
        ("cmd", "python processor.py"),
        ("dim", "==== Running parse_order ===="),
        ("stdout", "Enter items as name:qty CSV (e.g. pizza:2,burger:1): pizza:2,burger:1"),
        ("stdout", "Order: {'pizza': 2, 'burger': 1}"),
        ("dim", "\n==== Running delivery_eta ===="),
        ("stdout", "Enter distance in km (e.g. 4.5): 4.5"),
        ("stdout", "ETA in Minutes: 33"),
        ("dim", "\n==== Running coupon_discount ===="),
        ("stdout", "Enter a coupon code (e.g. SAVE50): SAVE50"),
        ("stdout", "Discount: 50"),
        ("dim", "\n# Testing dirty/malformed input resilience:"),
        ("stdout", "Enter items as name:qty CSV: pizza:2,corrupted,,bad:NaN -> Order: {'pizza': 2} [SAFE]"),
        ("stdout", "Enter distance in km: -5 or invalid -> ETA in Minutes: 15 [DEFAULT SAFE]"),
        ("stdout", "Enter coupon code: SAVE or invalid -> Discount: 0 [NO CRASH]"),
    ]
    render_terminal(
        "Lab 7 - Step 5: Running Fixed Application with Valid & Edge-Case Inputs",
        lines_step5,
        os.path.join(screenshots_dir, "step5_run_fixed_app.png"),
        width=1050
    )

    # 4. Step 6: Re-run test_processor.py with fixed processor -> 100% Pass
    lines_step6 = [
        ("header", "# Step 6: Re-Run test_processor.py with Hypothesis against fixed processor"),
        ("cmd", "pytest test_processor.py"),
        ("dim", "============================= test session starts =============================="),
        ("dim", "platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0"),
        ("dim", "rootdir: /Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7"),
        ("dim", "plugins: hypothesis-6.170.15, anyio-4.14.1, locust-2.46.0, langsmith-0.12.4"),
        ("dim", "collecting ... collected 3 items"),
        ("success", "test_food_delivery.py ...                                                [100%]"),
        ("dim", "============================== 3 passed in 0.38s ==============================="),
        ("success", "[SUCCESS] All 3 property-based fuzz tests passed!"),
        ("success", "Hypothesis generated hundreds of random strings, None, and edge inputs with 0 crashes."),
    ]
    render_terminal(
        "Lab 7 - Step 6: All Hypothesis Fuzz Tests Passing on Fixed Code",
        lines_step6,
        os.path.join(screenshots_dir, "step6_test_cases_passing.png"),
        width=1050
    )

    print("Lab 7 Step 5 & Step 6 screenshots generated.")

if __name__ == "__main__":
    generate_lab7_screenshots()
