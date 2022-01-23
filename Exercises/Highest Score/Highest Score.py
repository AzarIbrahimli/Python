student_scores=input("Input a list of student scores : ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

# With max function  (super easy way)
#print(f"The highest score in the class is {max(student_scores)}")



highest_score=student_scores[0]
c=0
for score in student_scores:    
    if score>highest_score:
        highest_score=score
        c=c+1
    else:
        c=c+1
print(f"The highest score in the class is {highest_score}")



