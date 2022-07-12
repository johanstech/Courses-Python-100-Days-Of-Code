number = int(input("Which number do you want to check?\n"))

even = number % 2 == 0

if even:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
