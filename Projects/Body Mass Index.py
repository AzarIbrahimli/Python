#Day 3
height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=round(weight//(height**2))
if bmi<18.5:
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi} and you are Normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi} and you are Overwieght")
elif bmi<35:
    print(f"Your bmi is {bmi} and you are Obese")
else:
    print(f"Your bmi is {bmi} and you are Clinically obese")

