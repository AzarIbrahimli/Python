print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
result_bill= total_bill*(tip/100+1)
per_person_bill=result_bill/people
#round number without loss 0
per_person_bill="{:.2f}".format(per_person_bill)
print(f"Each person sgould pay: ${per_person_bill}")


