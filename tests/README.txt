LAPTOP ADVISOR - UNIT TESTS

Test File: test_engine.py

The test_engine.py file uses Python's unittest framework to test the Laptop Advisor expert system.

The tests load the rules from kb/laptop_rules.json and create an ExpertSystem using different sets of input facts. Each test checks whether the expected conclusion is generated.

TEST CASES

1. Premium Ultrabook
   Input Facts:
   - budget_high
   - portable
   - long_battery

   Expected Output:
   - recommend:premium_ultrabook

2. Budget Ultrabook
   Input Facts:
   - budget_low
   - office_only
   - portable

   Expected Output:
   - recommend:budget_ultrabook

3. Gaming Laptop
   Input Facts:
   - gaming
   - budget_medium

   Expected Output:
   - recommend:midrange_gaming_laptop

4. High-End Gaming Laptop
   Input Facts:
   - gaming
   - budget_high

   Expected Output:
   - recommend:high_end_gaming_laptop

5. Creative Work RAM
   Input Facts:
   - creative_work
   - portable

   Expected Output:
   - spec:ram_16_plus

6. Creative Work Display
   Input Facts:
   - creative_work
   - large_screen

   Expected Output:
   - spec:display_15_plus_color_accurate

7. Travel Battery
   Input Facts:
   - travel_often
   - long_battery

   Expected Output:
   - spec:battery_60wh_plus

8. macOS Preference
   Input Facts:
   - pref_os_macos

   Expected Output:
   - spec:macos_required

9. AI Acceleration
   Input Facts:
   - needs_ai_accel

   Expected Output:
   - spec:gpu_with_tensor_cores

10. Linux Suitability
    Input Facts:
    - pref_os_linux
    - office_only

    Expected Output:
    - spec:linux_friendly_hw

11. No Matching Rules
    Input Facts:
    - None

    Expected Output:
    - Empty results (no conclusions)

HOW TO RUN THE TESTS

Open a terminal in the main project folder and run:

python3 -m unittest discover -s tests -v

TEST RESULTS

All 11 unit tests passed successfully.

The tests verify that each of the 10 rules produces the expected conclusion and that the system returns no conclusions when no rules match.