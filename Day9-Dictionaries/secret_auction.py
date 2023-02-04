import os
from secret_auction_art import logo

accepting_bids = True
accepted_bids = {}

print(logo)
print("Welcome to the secret auction program.")

while accepting_bids:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n$"))
    accepted_bids[name] = bid
    other_bidders = input("Any other bidders? (yes/no)\n").lower()
    if other_bidders == "yes":
        os.system("cls")
    else:
        accepting_bids = False


def highest_bidder(bids):
    name = ""
    bid = 0
    for key in bids:
        if bids[key] > bid:
            name = key
            bid = bids[key]
    print(f"The winner is {name} with a bid of ${bid}.")


highest_bidder(accepted_bids)
