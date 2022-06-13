import random
def start():
  name = input("Enter your name:")
  options = ["R","P","S"]
  print(f"Welcome {name}")
  users_turn = input("pick an option between R, P, or s:")
  if users_turn.upper() == random.choice(options):
    print(f"player({users_turn.upper()}):CPU({random.choice(options)})")
    print("It's a tie!...Try again")
    start()
  elif users_turn.upper()== "R" and random.choice(options)=="P":
    print("player(rock):CPU(paper)")
    print("Paper covers rock, CPU is the winner!")
  elif users_turn.upper()== "R" and random.choice(options)=="S":
    print("player(rock):CPU(scissors)")
    print("Rock smashes scissors, You are the winner!")
  elif users_turn.upper()=="S" and random.choice(options)=="P":
    print("player(scissors):CPU(paper)")
    print("Scissors cuts paper, You are the winner!")
  elif users_turn.upper()=="S" and random.choice(options)=="R":
    print("player(scissors):CPU(rock)")
    print("Rock smashes scissors, CPU is the winner!")
  elif users_turn.upper()=="P" and random.choice(options)=="S":
    print("player(paper):CPU(scissors)")
    print("Scissors cuts paper, CPU is the winner!")
  elif users_turn.upper()=="P" and random.choice(options)=="R":
    print("paper covers rock, player(paper):CPU(rock)")
    print("You are the winner!")
  else :
    print("Incorrect entry. Try again!")
    start()

start()
  
  