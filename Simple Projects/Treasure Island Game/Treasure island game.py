#Day 3 Final
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Tresure Island")
print("Your mission is to find the treasure.")
#print('You\'re beautiful')
direction=input('You\' re at a crossroad, where do you want to go? Type"Left or Right". ')
direction=direction.lower()
if direction!="left":
    print("You fell into a hole.Game over")
else: #lower in shortcase
    action=input('You\'ve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat.\nType "swim" to swim across. ').lower()
    if action != "wait":
        print("You got attacked by an angry trout.Game over")
    else:
        door=input("Which door? Red, Blue or Yellow ").lower()
        if door !="yellow":
            print("Game over")
        else:
            print("You find the treasure! You Win! ")
        

        

















