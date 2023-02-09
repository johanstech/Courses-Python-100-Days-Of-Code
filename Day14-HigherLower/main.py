import os
import random
from art import logo, vs
from data import data


def clear_and_logo():
    """Clear the screen and print logo."""
    os.system("cls")
    print(logo)


def get_account():
    """Get random account."""
    return random.choice(data)


def format_account(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def compare_followers(a, b):
    """Return if account a has a higher follower count than account b."""
    account_a_followers = a["follower_count"]
    account_b_followers = b["follower_count"]
    return account_a_followers > account_b_followers


def check_guess(a, b):
    """Check guess and return result."""
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess != "a" and guess != "b":
        while guess != "a" and guess != "b":
            guess = input(
                "Invalid input, try again.\nWho has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        return compare_followers(b, a)
    else:
        return compare_followers(a, b)


def higher_lower():
    score = 0
    game_over = False
    account_a = None
    while not game_over:
        clear_and_logo()
        if score != 0:
            print(f"You guessed correct! Current score: {score}")
        if account_a == None:
            account_a = get_account()
        account_b = get_account()
        if account_a["name"] == account_b["name"]:
            while account_a["name"] == account_b["name"]:
                account_b = get_account()
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Compare B: {format_account(account_b)}")
        game_over = check_guess(account_a, account_b)
        if not game_over:
            score += 1
            account_a = account_b
        else:
            clear_and_logo()
            print(f"Sorry, that's incorrect. Final score: {score}")
    again = input("Do you want to play again? (yes/no)\n").lower()
    if again == "yes" or again == "y":
        higher_lower()


higher_lower()
