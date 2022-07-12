print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

names = name1 + name2

true_total = 0
true_total += names.count("t")
true_total += names.count("r")
true_total += names.count("u")
true_total += names.count("e")

love_total = 0
love_total += names.count("l")
love_total += names.count("o")
love_total += names.count("v")
love_total += names.count("e")

total_string = str(true_total) + str(love_total)

total = int(total_string)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total <= 50 and total >= 40:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
