#Day 4 Who will pay the bill
import random
'''number=int(input("How many people there are?"))
c=0
names=[]
while c<number:
    names.append(input("Names? :"))
    c=c+1
print(names[random.randint(0,number)])'''

names=input("Give me everybody's names, seperated by a comma. ").split(",")
#a=names_.split(",")
'''choice=random.choice(names)
print(choice)'''
number=len(names)
choice=random.randint(0,(number-1))
print(names[choice]+" is going to buy the meal today")


#Input items to list by user
"""names=input("name: ").split(" ")
print(names)"""
