import random


class Card:
  def __init__(card):
    rank = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card.rank = random.choice(rank);
    suit = ["Hearts", "Diamonds", "Spade", "Clover"]
    card.suit = random.choice(suit);
  def displayNumber(card):
      print ("rank is " + card.rank)
  def displaySuit(card):
      print("suit is " + card.suit)

print("Eliot")
eliot = Card();
eliot.displayNumber();
eliot.displaySuit();
print("")
print("Sohum")
Sohum = Card();
Sohum.displayNumber();
Sohum.displaySuit();



# items = ["apple", "banana", "cherry"]
# random_item = random.choice(items)
# print(random_item)
