height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")

bmi = round(float(weight) / float(height) ** 2)

print(f"Your BMI is {bmi}.")
