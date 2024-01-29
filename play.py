import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def game():
  computer = [rock, paper, scissors]



  user = int(input("Which one do you choose rock (0), paper (1) or scissors? (2): "))
  print(computer[user])

  print("AI chose")
  ai = random.randint(0, 2)
  print(computer[ai])


  if user >= 3 or user <= 0:
    print("invalid command")
  elif (user == 0) and (ai == 1):
    print("You lost")
  elif (user == 0) and (ai == 1):
    print("draw")
  elif user == 0 and ai == 1:
    print("You win")
  elif user == 1 and ai == 1:
    print("Draw")
  elif user == 1 and ai == 0:
    print("você ganhou")
  elif user == 1 and ai == 2:
    print("You lost")
  elif user == 2 and ai == 2:
    print("empate")
  elif user == 2 and ai == 0:
    print("You lost")
  elif user == 2 and ai == 1:
    print("You win")

while True:
  game()