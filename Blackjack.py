import random

totalCards = [
  "King",
  "King", 
  "King",
  "King",
  "Queen",
  "Queen",
  "Queen", 
  "Queen",
  "Jack",
  "Jack", 
  "Jack", 
  "Jack", 
  ]
  
print ("Welcome to blackjack, ready?")
response = input("")

card1 = random.choice(totalCards)
card2 = random.choice(totalCards)
# remove card1 from deck, and remove card2
print("Your first card is " + card1 + " Your second card is " + card2)

dealerCard1 = random.choice(totalCards)
dealerCard2 = random.choice(totalCards)

print("")
print("Dealer's first card is " + card1)
print("")

userAction = input("What would you like to do? Hit or Stay")

if userAction == "Hit":
  card





how to remove a specifci element from a list
