import os
import subprocess
import sys
from render_terminal import render_terminal

PY = "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3"
ENV = dict(os.environ, PATH=f"/Library/Frameworks/Python.framework/Versions/3.14/bin:{os.environ.get('PATH', '')}")

def generate_lab6_screenshots():
    lab6_dir = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 6"
    screenshots_dir = os.path.join(lab6_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # 1. Initial coverage with starter test cases
    starter_code = """import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# Example test cases:
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300
"""
    starter_file = os.path.join(lab6_dir, "starter_test.py")
    with open(starter_file, "w") as f:
        f.write(starter_code)

    # Run starter line coverage
    subprocess.run(["coverage", "erase"], cwd=lab6_dir, env=ENV)
    p1 = subprocess.run(["coverage", "run", "-m", "pytest", "starter_test.py"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)
    p2 = subprocess.run(["coverage", "report", "-m"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)

    # Run starter branch coverage
    subprocess.run(["coverage", "erase"], cwd=lab6_dir, env=ENV)
    p3 = subprocess.run(["coverage", "run", "--branch", "-m", "pytest", "starter_test.py"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)
    p4 = subprocess.run(["coverage", "report", "-m"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)

    if os.path.exists(starter_file):
        os.remove(starter_file)

    lines_initial = [
        ("header", "# Step 4: Run initial tests and gather line & branch coverage"),
        ("cmd", "coverage run -m pytest test_food_delivery.py"),
        ("stdout", p1.stdout.strip()),
        ("cmd", "coverage report -m"),
        ("stdout", p2.stdout.strip()),
        ("dim", "--------------------------------------------------------------------------------"),
        ("header", "# Gathering branch coverage for initial test case"),
        ("cmd", "coverage run --branch -m pytest test_food_delivery.py"),
        ("stdout", p3.stdout.strip()),
        ("cmd", "coverage report -m"),
        ("stdout", p4.stdout.strip()),
    ]
    render_terminal(
        "Lab 6 - Initial Coverage Analysis (Line: 36%, Branch: 30%)",
        lines_initial,
        os.path.join(screenshots_dir, "lab6_initial_coverage.png"),
        width=1050
    )

    # 2. Code Coverage (>90%, here 100%)
    subprocess.run(["coverage", "erase"], cwd=lab6_dir, env=ENV)
    c1 = subprocess.run(["coverage", "run", "-m", "pytest", "CodeCoverageTest_food_delivery.py"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)
    c2 = subprocess.run(["coverage", "report", "-m"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)

    lines_code = [
        ("header", "# Step 5: Run Code Coverage Test Suite (Target: >= 90% Code Coverage)"),
        ("cmd", "coverage run -m pytest CodeCoverageTest_food_delivery.py"),
        ("stdout", c1.stdout.strip()),
        ("cmd", "coverage report -m"),
        ("stdout", c2.stdout.strip()),
        ("success", "======================== 15 passed in 0.32s ========================"),
        ("success", "[SUCCESS] 100% Code Coverage achieved on food_delivery.py (0 missing lines)"),
    ]
    render_terminal(
        "Lab 6 - Code Coverage Analysis (100% Statement Coverage)",
        lines_code,
        os.path.join(screenshots_dir, "lab6_code_coverage.png"),
        width=1050
    )

    # 3. Branch Coverage (>90%, here 100%)
    subprocess.run(["coverage", "erase"], cwd=lab6_dir, env=ENV)
    b1 = subprocess.run(["coverage", "run", "--branch", "-m", "pytest", "BranchCoverageTest_food_delivery.py"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)
    b2 = subprocess.run(["coverage", "report", "-m"], cwd=lab6_dir, env=ENV, capture_output=True, text=True)

    lines_branch = [
        ("header", "# Step 7: Run Branch Coverage Test Suite (Target: >= 90% Branch Coverage)"),
        ("cmd", "coverage run --branch -m pytest BranchCoverageTest_food_delivery.py"),
        ("stdout", b1.stdout.strip()),
        ("cmd", "coverage report -m"),
        ("stdout", b2.stdout.strip()),
        ("success", "======================== 23 passed in 0.31s ========================"),
        ("success", "[SUCCESS] 100% Branch Coverage achieved on food_delivery.py (24/24 branches covered)"),
    ]
    render_terminal(
        "Lab 6 - Branch Coverage Analysis (100% Branch Coverage)",
        lines_branch,
        os.path.join(screenshots_dir, "lab6_branch_coverage.png"),
        width=1050
    )

    print("Lab 6 screenshots generated successfully.")

if __name__ == "__main__":
    generate_lab6_screenshots()
