#Day 4 Project (Rock,paper and scissors Game)
import random
game=[''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' ,''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''  ]
my_choise=int(input("What do you choose?\nType 0 for Rock\n1 for Paper\n2 for Scissors."))
while my_choise>2:
    my_choise=int(input("What do you choose?\nType 0 for Rock\n1 for Paper\n2 for Scissors."))    
comp_choise=random.randint(0,2)
print(game[my_choise])
print(game[comp_choise])
if my_choise==comp_choise:
    print("Draw")
elif (my_choise ==0 and comp_choise==2) or (my_choise ==1 and comp_choise==0) or (my_choise ==2 and comp_choise==1):
    print("You win")
else:
    print("Comp win")
    









