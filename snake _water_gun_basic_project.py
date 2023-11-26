import random

while True: 
 choices = ["gun","water","snake"]

 computer = random.choice(choices)

 player = None

 while player not in choices:
    player = input("gun, water, or snake?: ").lower()

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

 if play_again != "yes":
   break

print("Bye!!!")




