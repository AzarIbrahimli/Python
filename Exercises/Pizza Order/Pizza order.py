#Day3
print("Welcome to Python Azar Pizza Deliveries!")
size= input("What size pizza do you want? : S, M or L ")
add_pepperoni=input("Do you want to add pepperoni? Y or N ")
add_cheese=input("Do you want extra cheese? Y or N ")
bill=0
if size=="S":
    bill=bill+15
    if add_pepperoni=="Y":
        bill=bill+2
    else:
         print(f"Your bill is ${bill}")         
    if add_cheese=="Y":
        bill=bill+1
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")       
elif size=="M" or size=="L":
    if size=="M":
        bill=bill+20
    elif size=="L":
        bill=bill+25
    if add_pepperoni=="Y":
        bill=bill+3
    else:
         print(f"Your bill is ${bill}")         
    if add_cheese=="Y":
        bill=bill+1
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")       

    
    

