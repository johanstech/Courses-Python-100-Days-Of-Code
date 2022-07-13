height = float(input("Enter your height in m:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = round(weight / height ** 2)

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi > 18.5:
    print(f"Your BMI is {bmi}, you are normal weigh.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")
