import os
import random
from art import logo


def deal_card(hand):
    """Deal a random card to hand."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101, 102, 103]
    hand.append(random.choice(cards))


def initial_deal(player_hand, dealer_hand):
    """Deal initial cards to player and dealer."""
    for _ in range(2):
        deal_card(player_hand)
        deal_card(dealer_hand)


def pretty_card(card):
    if card == 1 or card == 11:
        return "Ace"
    elif card == 101:
        return "Knight"
    elif card == 102:
        return "Queen"
    elif card == 103:
        return "King"
    else:
        return card


def print_hand(text, hand, dealer_and_initial):
    pretty_hand = []
    if dealer_and_initial:
        pretty_hand = [pretty_card(hand[0]), "?"]
    else:
        for card in hand:
            pretty_hand.append(pretty_card(card))
    print(text, pretty_hand)


def blackjack(hand):
    if 11 in hand:
        if 10 in hand or 101 in hand or 102 in hand or 103 in hand:
            return True
    return False


def sum_of_cards(hand):
    """Return sum of cards in hand."""
    sum_hand = 0
    for card in hand:
        if card == 101 or card == 102 or card == 103:
            sum_hand += 10
        else:
            sum_hand += card
    if sum_hand > 21 and 11 in hand:
        i = hand.index(11)
        hand[i] = 1
        sum_hand -= 10
    return sum_hand


def player_turn(hand):
    """Player turn."""
    playing = True
    while playing:
        current_sum = sum_of_cards(hand)
        if current_sum > 21:
            playing = False
            print(f"{current_sum} is a bust! You lose.")
            return True
        else:
            action = input(
                "Do you want to hit or stand? (hit/stand)\n").lower()
            if action == "hit" or action == "h":
                deal_card(hand)
                print_hand("Your hand:", hand, False)
            else:
                playing = False
    return False


def dealer_turn(hand):
    """Dealer turn."""
    playing = True
    while playing:
        current_sum = sum_of_cards(hand)
        if current_sum > 21:
            playing = False
            print(f"{current_sum} is a bust! You win!")
            return True
        else:
            if current_sum <= 16:
                deal_card(hand)
                print_hand("Dealer's hand:", hand, False)
            else:
                playing = False
    return False


def play_blackjack():
    # Clear screen and print logo
    os.system("cls")
    print(logo)
    # Set and print initial hand
    player_hand = []
    dealer_hand = []
    initial_deal(player_hand, dealer_hand)
    print_hand("Your hand:", player_hand, False)
    print_hand("Dealer's hand:", dealer_hand, True)
    if blackjack(player_hand):
        print("Blackjack! You win!")
    else:
        player_bust = player_turn(player_hand)
        if not player_bust:
            print_hand("Dealer's hand:", dealer_hand, False)
            if blackjack(dealer_hand):
                print("Blackjack! The house wins.")
            else:
                dealer_bust = dealer_turn(dealer_hand)
                if not dealer_bust:
                    player_sum = sum_of_cards(player_hand)
                    dealer_sum = sum_of_cards(dealer_hand)
                    if player_sum == dealer_sum:
                        print(f"It's a push with double {player_sum}'s.")
                    elif player_sum > dealer_sum:
                        print(
                            f"You win with {player_sum} against {dealer_sum}!")
                    else:
                        print(
                            f"The house wins with {dealer_sum} against {player_sum}.")
    again = input("Do you want to play again? (yes/no)\n").lower()
    if again == "yes" or again == "y":
        play_blackjack()


play = input("Do you want to play a game of Blackjack? (yes/no)\n").lower()
if play == "yes" or play == "y":
    play_blackjack()
