from random import choice  # , randint

names_string = input("Enter the participants' names, separated by comma.\n")
names = names_string.split(", ")

# loser = names[randint(0, len(names) - 1)]

loser = choice(names)
print(f"{loser} has to pay the bill!")
