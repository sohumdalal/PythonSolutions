import time

board = [
  ["1","2","3"],
  ["4","5","6"],
  ["7","8","9"]
  ]

def printBoard():
  for element in board:
    print(element)
    
def giveMeSpaceAndTime():
  time.sleep(1)
  print("")


print("Welcome to Tic Tac Toe, I assume you are two people, so you will pass the computer back and forth!")
print("")
time.sleep(2)
ready = input("ready to get started?")

if ready == "yes":
  print("great")
  giveMeSpaceAndTime();
  print("Here is our board")
  printBoard()
  giveMeSpaceAndTime();
  print("go ahead and input a number, and your symbol, and I will update the board")
else:
  print("let me know when you are ready!")


