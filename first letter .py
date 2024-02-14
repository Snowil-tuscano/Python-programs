def digit(n):
    sum=0
    for x in str(n):
        sum+=int(x)
    print(sum)
    
x= int(input(" enter a number "))
digit(x)