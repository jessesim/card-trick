# CardTrick.py

import random

def main():
    # Declare variables
    column = 0
    loopCounter = 0

    # Declare the deck list
    deck = [0] * 52

    # Declare a 7 row by 3 column list
    #play = [[0, 0, 0]] * 7

    cols = 3
    rows = 7
    play = [[int for _ in range(cols)] for _ in range(rows)]

    # Openning message
    print("Welcome.  I'm not the latest development in AI, but ")
    print("I'm a computer program that can performa card trick.")
    print("Let's begin!")
    print()
    print("Building the deck of cards...")

    # Call BuildDeck()
    BuildDeck(deck)

    print("Done! \n")
    seeDeck = input("Now would you like to see the deck (y/n)?")
    
        # Call PrintDeck()
    if seeDeck.lower() == 'y':
        PrintDeck(deck)

    # Begin the main card trick loop
    for loopCounter in range(3):
        # Call Deal()
        Deal(deck, play)

        column = int(input("\nWhich column is your card in (0, 1, or 2)?: "))

        # Call PickUp()
        PickUp(deck, play, column)

    # Call SecretCard()
    SecretCard(deck)

    print("Thank you for playing the card trick!")


def PrintCard(card):
    rank = card % 13
    suit = card // 13

    if rank == 0:
        cardString = "  King of "
    elif  rank == 1:
        cardString = "   Ace of "
    elif  rank == 11:
        cardString = "  Jack of "
    elif  rank == 12:
        cardString = " Queen of "
    else: 
        cardString = f"{rank: 6d} of "

    
    if suit == 0:
        cardString += "Clubs     "
    elif suit == 1:
        cardString += "Hearts    "
    elif  suit == 2:
        cardString += "Diamonds  "
    elif  suit == 3:
        cardString += "Spades    "

    print(cardString, end='')


def BuildDeck(deck):
    # Define local variables
    used = [0] * 52
    card = 0
    i = 0

    # Generate cards until the deck is full of integers
    while i < 52:
        # Generate a random integer between 0 and 51
        card = random.randint(0,51)

        # Test to see if the value has already been used
        # If not, add it to the deck
        if used[card] == 0:
            used [card] = 1
            deck[i] = card
            i += 1

        
    # End while loop
    


def PrintDeck(deck):
    # Define local variables
    for card in deck:
        PrintCard(card)
        print()

    
        
    # End for loop


def Deal(deck, play):
    # Define local variables
    card = 0

    # Deal the cards from the deck to the play list
    print()
    print("   Column 0           Column 1           Column 2")
    print("=======================================================")

    #nested loop to deal cards
    for row in [0,1,2,3,4,5,6]:
        for column in [0,1,2]:
            play[row][column] = deck[card]
            PrintCard(play[row][column])
            card += 1
        print()
    
    # End nested for loop structure
    


def PickUp(deck, play, column):
    # Define local variables
    card = 0
    row = 0
    first = 0
    last = 0
    # Identify the order of columns to pick up
    if column == 0:
        first = 1
        last = 2
    elif column == 1:
        first = 0
        last = 2
    else:
        first = 0
        last = 1

    # Now pick up cards from the play list by column and put them in deck
    for row in [0,1,2,3,4,5,6]:
        deck[card] = play[row][first]
        card += 1

    for row in [0,1,2,3,4,5,6]:
        deck[card] = play[row][column]
        card += 1

    for row in [0,1,2,3,4,5,6]:
        deck[card] = play[row][last]
        card += 1
    
    # End for loop structure
    

def SecretCard(deck):
    # Define local variables
    card = 0

    print()
    print("Finding secret card...")
    for card in range(0, 10):
        PrintCard(deck[card])
        print()

    print("Your secret card is: ", end='')
    card += 1
    PrintCard(deck[card])
    print()
    

main()        
