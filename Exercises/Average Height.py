height=input("Enter a list of student heights,pelase : ").split()
total_height=0
for n in range(0, len(height)):
    total_height=total_height+int(height[n])
average=total_height/(n+1)
print(f"Average is {round(average)}")         


    
