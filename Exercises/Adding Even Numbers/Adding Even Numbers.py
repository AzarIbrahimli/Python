my_range=input("Enter a range, please : ").split()
for n in range(0,len(my_range)):
    my_range[n]=int(my_range[n])
first=my_range[0]
second=my_range[1]
sum=0
if (first%2==0 and second%2!=0) :
    for number in range(first,second, 2):
        sum=sum+number
elif (first%2==0 and second%2==0):
    for number in range(first,second+1, 2):
        sum=sum+number
elif first%2!=0 and second%2!=0:
    for number in range(first+1,second, 2):
        sum=sum+number
elif (first%2!=0 and second%2==0):
    for number in range(first+1,second+1, 2):
        sum=sum+number
print(sum)    
