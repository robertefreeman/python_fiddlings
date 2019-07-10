'''
Rob Jack: A simple blackjack game
'''

import random

import os


def clear(): return os.system('clear')


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return '{self.rank} of {self.suit}'.format(self=self)


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        return '[%s]' % ', '.join(map(str, self.deck))

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        # print('Deck Shuffled')

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces = 1

    def __str__(self):
        return '[%s]' % ', '.join(map(str, self.cards))

    def adjust_for_ace(self):
        if self.value > 21:
            if self.aces == 1:
                self.value = self.value - 10
                self.aces = 0


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def __str__(self):
        return '{self.total}'.format(self=self)

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0


def take_bet(bank):
    wager = int(input('How much would you like to bet: '))
    while True:
        if wager >= 0 and wager <= 100:
            return wager
        else:
            wager = input(
                'You dont have enough money, how much would you like to bet: ')
            pass


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    if (input('\nDo you want to hit or stand? ').lower() == 'hit'):
        hit(deck, hand)
    else:
        playing = False


def show_some(player, dealer):
    print("Player's Hand: " + str(player.value) + '\n\n' + str(player))
    print("\nDealer's Hand:\n\n[" + str(dealer.cards[0]) + ', ** Flipped **]')


def show_all(player, dealer):
    print("Player's Hand: " + str(player.value) + '\n\n' + str(player))
    print("\nDealer's Hand: " + str(dealer.value) + '\n\n' + str(dealer))


def player_busts(bank):
    print('You busted!!!')
    bank.lose_bet()


def player_wins(bank):
    print('You won!!!')
    bank.win_bet()


def dealer_busts(bank):
    print('You won, the dealer busted')
    bank.win_bet()


def dealer_wins(bank):
    print('The dealer wins!')
    bank.lose_bet()


def push():
    print('Its a push!')


bank = Chips()

while True:
    wager = 0
    # Print an opening statement

    clear()
    print('Welcome to RobJack')

    # Create & shuffle the deck, deal two cards to each player

    vegas_deck = Deck()
    vegas_deck.shuffle()
    p1_hand = Hand()
    d_hand = Hand()
    p1_hand.add_card(vegas_deck.deal())
    p1_hand.add_card(vegas_deck.deal())
    d_hand.add_card(vegas_deck.deal())
    d_hand.add_card(vegas_deck.deal())

    # Set up the Player's chips

    print('Your Current bank is bank: ' + str(bank) + '\n')

    # Prompt the Player for their bet

    bank.bet = take_bet(bank)

    # Show cards (but keep one dealer card hidden)

    show_some(p1_hand, d_hand)

    while playing:
        # Prompt for Player to Hit or Stand

        if p1_hand.value > 21:
            player_busts(bank)
            break
        else:
            pass

        hit_or_stand(vegas_deck, p1_hand)

        # Show cards (but keep one dealer card hidden)

        show_some(p1_hand, d_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        if p1_hand.value > 21:
            player_busts(bank)
            break
        else:
            pass

    # Reset playing global variable
    playing = True

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if p1_hand.value <= 21:
        while d_hand.value < 17:
            hit(vegas_deck, d_hand)
        show_all(p1_hand, d_hand)

        # Run different winning scenarios

        if d_hand.value > 21:
            dealer_busts(bank)
        elif d_hand.value > p1_hand.value:
            dealer_wins(bank)
        elif p1_hand.value > d_hand.value:
            player_wins(bank)
        else:
            push()

    # Inform Player of their chips total

    print('Your Current bank is bank: ' + str(bank) + '\n')

    # Ask to play again
    if input('\n\n\nDo you want to play again (Y of N)?: ').lower() == 'y':
        pass
    else:
        break
