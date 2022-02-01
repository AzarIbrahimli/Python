import math
def calculate(height,width,coverage):
    number_of_cans=(height*width)/coverage
    print(f"You need {math.ceil(number_of_cans)} cans of paint")
my_height=int(input("Height: "))
my_width=int(input("Width: "))
my_coverage=int(input("Coverage: "))
calculate(height=my_height,width=my_width,coverage=my_coverage)
