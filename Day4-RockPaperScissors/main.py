from random import randint

draw = "It's a draw..."
win = "You win!"
lose = "You lose."

player = input(
    'Rock, paper, scissors!\nType "rock", "paper", or "scissors" to make your choice!\n').lower()

random_number = randint(1, 3001)
if random_number > 2000:
    computer = "scissors"
elif random_number > 1000:
    computer = "paper"
else:
    computer = "rock"

outcome = f"You played {player} and computer played {computer}."
if player == computer:
    print(f"{outcome} {draw}")
elif player == "rock":
    if computer == "paper":
        print(f"{outcome} {lose}")
    else:
        print(f"{outcome} {win}")
elif player == "paper":
    if computer == "scissors":
        print(f"{outcome} {lose}")
    else:
        print(f"{outcome} {win}")
elif player == "scissors":
    if computer == "rock":
        print(f"{outcome} {lose}")
    else:
        print(f"{outcome} {win}")
else:
    print(f'"{player}" is not valid input...')
