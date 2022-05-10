import os
import random

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4 

def deal(deck):
  hand = []
  for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:card = 'J'
    if card == 12:card = 'Q'
    if card == 13:card = 'K'
    if card == 13:card = 'A'
    hand.append(card)
  return hand

def play_again():
  again = raw_input("do you want to play again? (Y/N) : ").lower()
  if again == "Y":
    dealer_hand = []
    player_hand = []
    deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
    game()
  
  else:
    print("bye!")
    exit()

def total(hand):
  total = 0
  for card in hand:
    if card == 'J' or card == 'Q' or card == 'K':
      total+= 10
    elif card == 'A':
      if total >= 11: total += 1
      else: total += 11
    else: 
      total += card
    return total

def hit(hand):
  card = deck.pop()
  if card == 11: card = 'J'
  if card == 12: card = 'Q'
  if card == 13: card = 'K'
  if card == 14: card = 'A'
  hand.append(card)
  return hand

def clear():
  if os.name == 'nt':
    os.system('CLS')
  if os.name == 'posix':
    os.system('clear')

def print_results(dealer_hand, player_hand):
  clear()
  print "the dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
  print "you have a " + str(player_hand) + " for a total of " + str(total(player_hand))

def blackjack(dealer_hand, player_hand):
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print "congratulations! you got blackjack!\n"
    play_again()
  elif total(dealer_hand) == 21:
    print_results(dealer_hand, player_hand)
    print "dealer has blackjack, you lose.\n"
    play_again()

def score(dealer_hand, player_hand):
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print "congratulations! you got blackjack!\n"
  elif total(dealer_hand) == 21:
    print_results(dealer_hand, player_hand)
    print "dealer has blackjack, you lose.\n"
  elif total(player_hand) > 21:
    print_results(dealer_hand, player_hand)
    print "you have busted, you lose.\n"
  elif total(dealer_hand) > 21:
    print_results(dealer_hand, player_hand)
    print "dealer busts, you win!\n"
  elif total(player_hand) < total(dealer_hand):
    print_results(dealer_hand)
    
  

