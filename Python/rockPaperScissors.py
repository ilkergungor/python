import random

while True:

      choices = ["rock", "paper", "scissors"]

      computer = random.choice(choices)
      player = None

      while player not in choices:  #!CUZ IT IS NONE FOR NOW
            player = input("rock, paper, scissors: ").lower()

      if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("TIE!")

      elif player == "rock":
            if computer == "paper":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU LOSE!")   
            if computer == "scissors":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU WIN!")     

      elif player == "paper":
            if computer == "scissors":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU LOSE!")    
            if computer == "rock":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU WIN!")     

      elif player == "scissors":
            if computer == "rock":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU LOSE!")          
            if computer == "paper":
                  print("computer: ", computer)
                  print("player: ", player)
                  print("YOU WIN!")     

      play_again = input("Play again? (Y/N): ").lower()

      if play_again != "y":
            break

print("Bye!")


