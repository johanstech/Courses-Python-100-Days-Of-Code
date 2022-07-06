print("Welcome to the tip calculator.")

total = float(input("What was the total bill? "))
people = float(input("How many people to split the bill? "))
percentage = float(input(
    "What percentage tip would you like to give? 10, 15, or 20? "))
tip = percentage / 100 + 1

split = round(total * tip / people, 1)

print(f"Each person should pay: {split}")
