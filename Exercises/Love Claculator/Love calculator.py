#Day3
print("Welcome to the Love Calculator! ")
name1=input("What is your name? : ")
name2=input("What is his/her name? : ")
#name=Azar
#x=name.lower()  x=azar
name=name1+name2
name=name.lower()
#c=name.count("a")  c=2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")

sum_true=t+r+u+e
sum_love=l+o+v+e
score=int(str(sum_true) + str(sum_love))
if score <10 or score > 90:
    print(f"Your score is {score}%,you go together like coke and mentos")
elif score >40 and score< 50:
    print(f"Your score is {score}%,you are alright together")
else:
    print(f"Your score is {score}%")


