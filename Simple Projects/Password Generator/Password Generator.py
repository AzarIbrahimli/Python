import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=[]
print("Welcome to the PyPassword Generator!")
letter_number=int(input("How many letters would you like in your password? :"))
symbol_number=int(input("How many symbols would you like? :"))
number_numb=int(input("How many numbers would you like? :"))
for n in range(0,letter_number):
    letter=random.choice(letters)
    password.append(letter)
#   print(letter)
for n in range(0,symbol_number):
    symbol=random.choice(symbols)
    password.append(symbol)
#    print(symbol)
for n in range(0,number_numb):
    number=random.choice(numbers)
    password.append(number)

# This is for changing position of the elements of the sequence
random.shuffle(password)
#First method
print("Here is your password : ", end="")
print(*password, sep="")
#This reduce comma and brackets in list 


#Second method 
"""passwordlist=""
for x in password:
    passwordlist=str(passwordlist)+x
print(passwordlist)    
"""
