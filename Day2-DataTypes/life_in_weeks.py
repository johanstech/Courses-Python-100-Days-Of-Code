age = input("What's your age?\n")

left_to_90 = 90 - int(age)

days_left = left_to_90 * 365
weeks_left = left_to_90 * 52
months_left = left_to_90 * 12

print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left until 90.")
