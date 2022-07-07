unexpected_input_ending = "Oops, looks like you wandered off and got eaten by a bear. Game over!"

print('Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou\'re at a crossroad. Where do you want to go? Type "left" or "right".')

choice1 = input()
if choice1 == "left":
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat, or "swim" to swim across.')
    choice2 = input()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a building with 3 coloured doors. One red, one yellow, and one blue. Which colour do you choose?")
        choice3 = input()
        if choice3 == "red":
            print("You enter the door and find yourself in a dark room. The floor suddenly opens to a pit of spikes. You're impaled. Game over!")
        elif choice3 == "yellow":
            print("You've found the treasure! You win!")
        elif choice3 == "blue":
            print(
                "You open the door to a room full of bloodthirsty beats, and now you're dinner. Game over!")
        else:
            print(unexpected_input_ending)
    elif choice2 == "swim":
        print("You don't get very far before you're eaten by a crocodile! Game over!")
    else:
        print(unexpected_input_ending)
elif choice1 == "right":
    print("You appear to have gotten lost in the woods, and starved to death. Game over!")
else:
    print(unexpected_input_ending)
