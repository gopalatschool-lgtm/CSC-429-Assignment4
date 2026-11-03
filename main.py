
import json
from engine import ExpertSystem


def load_rules():
    """
    Load the knowledge base from the JSON file.
    """

    with open("kb/laptop_rules.json", "r") as file:
        rules = json.load(file)

    return rules


def ask_yes_no(question):
    """
    Ask a yes/no question and return True or False.
    """

    while True:
        answer = input(question + " (y/n): ").strip().lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n.")


def collect_facts():
    """
    Ask the user about their laptop preferences.
    Convert their answers into facts.
    """

    facts = set()

    # Ask about the user's budget.
    print("\n--- Laptop Budget ---")

    while True:
        budget = input(
            "What is your budget? (low/medium/high): "
        ).strip().lower()

        if budget in ["low", "medium", "high"]:
            facts.add("budget_" + budget)
            break
        else:
            print("Please enter low, medium, or high.")

    # Ask about laptop usage and preferences.
    print("\n--- Laptop Preferences ---")

    questions = {
        "portable": "Is portability important?",
        "long_battery": "Do you need long battery life?",
        "gaming": "Will you use the laptop for gaming?",
        "creative_work": "Will you do creative work?",
        "office_only": "Will you use it for office work only?",
        "large_screen": "Do you need a large screen?",
        "travel_often": "Do you travel often?",
        "needs_ai_accel": "Do you need AI acceleration?"
    }

    # Add facts whenever the user answers yes.
    for fact, question in questions.items():
        if ask_yes_no(question):
            facts.add(fact)

    # Ask for operating system preference.
    print("\n--- Operating System ---")

    while True:
        os_choice = input(
            "Preferred OS? (windows/macos/linux): "
        ).strip().lower()

        if os_choice in ["windows", "macos", "linux"]:
            facts.add("pref_os_" + os_choice)
            break
        else:
            print("Please enter windows, macos, or linux.")

    return facts


def main():
    """
    Main program:
    1. Load rules.
    2. Collect facts.
    3. Run inference.
    4. Display recommendations.
    """

    print("================================")
    print("       LAPTOP ADVISOR")
    print("================================")

    # Load rules from the knowledge base.
    rules = load_rules()

    # Collect facts from the user.
    facts = collect_facts()

    # Create the expert system.
    system = ExpertSystem(rules, facts)

    # Run forward chaining.
    results = system.run()

    # Display the original user facts.
    print("\n================================")
    print("          RESULTS")
    print("================================")

    print("\nUser Facts:")

    for fact in sorted(facts):
        print("-", fact)

    # Display the rules that fired.
    print("\nRules Fired:")

    if system.fired_rules:
        for rule in system.fired_rules:
            print("-", rule["name"])
    else:
        print("No rules fired.")

    # Display recommendations and specifications.
    print("\nLaptop Recommendations:")

    recommendations = [
        item for item in results
        if item.startswith("recommend:")
    ]

    if recommendations:
        for item in recommendations:
            print("-", item.replace("recommend:", ""))
    else:
        print("No specific laptop recommendation found.")

    print("\nRecommended Specifications:")

    specifications = [
        item for item in results
        if item.startswith("spec:")
    ]

    if specifications:
        for item in specifications:
            print("-", item.replace("spec:", ""))
    else:
        print("No additional specifications found.")

    print("\n================================")
    print("       END OF ADVISOR")
    print("================================")


# Run the program.
if __name__ == "__main__":
    main()
