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


hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
list = [rock, paper, scissors]
print(list[hand])
comrand = random.randint(0,2)
print(f"Computer choose:\n{list[comrand]}")

diff = hand - comrand
if diff > 0 or diff == -2:
    print("You win")
elif diff == 0:
    print("draw")
elif diff == -1 or diff == 2:
    print("You lose")
    

