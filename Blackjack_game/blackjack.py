#import statements and variables
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#Classes definition
class Card():

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + 'of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with the same empty list every time
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # print each Card object
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		#passed card from Deck.deal()
		self.cards.append(card)
		self.value += values[card.rank]

		#keep number of aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):

		#If we score over 21, change ace from 21 to 1 
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1
		
class Chips:

	def __init__(self):
		self.total = 1000
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet 

#Functions definitions
def take_bet(chips):

	while True:
		try:
			chips.bet = int(input('How many chips will you bet?'))
		except:
			print('Please provide an integer')
		else:
			if chips.bet > chips.total:
				print('Sorry, not enough chips.')
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()			

def hit_or_stand(deck,hand):
	global playing
	while True:
		x = input('Hit or Stand? Press h or s')

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player stops, dealer's turn")
			playing = False
		else:
			print('Wrong input, press h or s')
			continue
		break

def show_some(player,dealer):
	print ('Dealers hand:')
	print('One card is hidden.')
	print(dealer.cards[1])
	print('\n')
	print('Players hand:')
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	print ('Dealers hand:')
	for card in dealer.cards:
		print(card)
	print('\n')
	print('Players hand:')
	for cards in player.cards:
		print(card)

def player_busts(player,dealer,chips):
	print('Player busted!')
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print('Player wins!')
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print('Dealer busted.Player wins!')
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print('Dealer wins!')
	chips.lose_bet()

def push(player,dealer):
	print("It's a tie!")


#Gameplay
while True:
	print('Welcome to Blackjack!')

	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#player chips
	player_chips = Chips()

	#ask for bet 
	take_bet(player_chips)

	#show cards(one hidden for dealer)
	show_some(player_hand,dealer_hand)

	while playing:

		#ask for hit or stand
		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)

			break

	#Dealers turn, if player has not busted
	if player_hand.value <=21:
		#if dealer less that 17, hit
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		#Check winning conditions
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	print("\n Players chips are ",player_chips.total)

	#Ask for new game
	new_game = input("Would you like a new game?y/n")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print('Thank you for playing.')
		break