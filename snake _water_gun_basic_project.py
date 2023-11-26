# importing important library 
import random

# putting a loop as a case; if case is true it will continue
while True: 
 choices = ["gun","water","snake"]

 computer = random.choice(choices)

 player = None

 while player not in choices:
    player = input("gun, water, or snake?: ").lower()

# A tie scenario in between computer and human 
 if player == computer:
    print("computer: ",computer)
    print("player: ",player)
    print("It's a tie brosky!!")

 elif player == "gun":
    if computer == "water":
     print("computer: ",computer)
     print("player: ",player)
     print("You lose!!")    
    if computer == "snake":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!!")

 elif player == "water":
    if computer == "gun":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!!")    
    if computer == "snake":
     print("computer: ",computer)
     print("player: ",player)
     print("You lose!!")

 elif player == "snake":
    if computer == "water":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!!")    
    if computer == "gun":
     print("computer: ",computer)
     print("player: ",player)
     print("You lose!!")

 play_again = input("Wanna have a rematch? (yes/no): ").lower()

 if play_again not in ["yes","y"]:
   break

print("Bye!!!")




