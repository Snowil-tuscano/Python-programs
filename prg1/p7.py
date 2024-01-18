a= int(input(" enter a number "))
b=int(input(" enter another number "))
print(f" before swapping {a} and {b} ")
tep = a
a=b
b=tep

print(f" after excahnging the values are {a } and {b}")

a=a+b
b= a-b
a = a-b
print(f" after excahnging the values are {a } and {b}")
