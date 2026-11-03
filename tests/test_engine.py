import unittest
import json
import os
import sys

# Allow Python to import engine.py from the parent folder.
sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from engine import ExpertSystem


class TestExpertSystem(unittest.TestCase):

    def setUp(self):
        # Load the rules from the knowledge base.
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "kb",
            "laptop_rules.json"
        )

        with open(path, "r") as file:
            self.rules = json.load(file)

    def test_premium_ultrabook(self):
        # Rule 1: High budget, portability, and long battery.
        facts = {"budget_high", "portable", "long_battery"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("recommend:premium_ultrabook", results)

    def test_budget_ultrabook(self):
        # Rule 2: Low budget, office use, and portability.
        facts = {"budget_low", "office_only", "portable"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("recommend:budget_ultrabook", results)

    def test_gaming_laptop(self):
        # Rule 3: Medium budget and gaming preference.
        facts = {"gaming", "budget_medium"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("recommend:midrange_gaming_laptop", results)

    def test_high_end_gaming(self):
        # Rule 4: High budget and gaming preference.
        facts = {"gaming", "budget_high"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("recommend:high_end_gaming_laptop", results)

    def test_creative_work(self):
        # Rule 5: Creative work and portability.
        facts = {"creative_work", "portable"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:ram_16_plus", results)

    def test_creative_work_display(self):
        # Rule 6: Creative work and large screen.
        facts = {"creative_work", "large_screen"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:display_15_plus_color_accurate", results)

    def test_travel_battery(self):
        # Rule 7: Frequent travel and long battery.
        facts = {"travel_often", "long_battery"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:battery_60wh_plus", results)

    def test_macos_preference(self):
        # Rule 8: macOS preference.
        facts = {"pref_os_macos"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:macos_required", results)

    def test_ai_acceleration(self):
        # Rule 9: User needs AI acceleration.
        facts = {"needs_ai_accel"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:gpu_with_tensor_cores", results)

    def test_linux_suitability(self):
        # Rule 10: Linux preference and office use.
        facts = {"pref_os_linux", "office_only"}
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertIn("spec:linux_friendly_hw", results)

    def test_no_matching_rules(self):
        # No facts should produce no conclusions.
        facts = set()
        system = ExpertSystem(self.rules, facts)
        results = system.run()
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()