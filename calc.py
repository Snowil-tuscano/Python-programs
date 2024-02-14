import math
name  = input(" enter the  name ")
age = int(input(" enter the age "))

if age>=18 and age<80:
    print(f"{name} is elgible for driving License ")
else:
    if age <=18:
        age = abs(age-18)
        print(f"{name} is not elgible for driving License , should wait for {age}  years to complete the requirement  ")
    elif age >=80:
        print(f"{name} is not elgible for driving License ,{age} as senior citizen")
