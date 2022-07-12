print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L?\n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N?\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N?\n").lower()

price = 15
if size == "l":
    price = 25
    if add_pepperoni:
        price += 3
elif size == "m":
    price = 20
    if add_pepperoni:
        price += 3
else:
    if add_pepperoni:
        price += 2

if extra_cheese:
    price += 1

print(f"Your total is ${price}.")
