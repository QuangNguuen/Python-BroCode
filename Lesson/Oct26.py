
def numRoot(a,b,c):
    det = b**2 - 4*a*c
    if det > 0:
        root1 = (-1*b + det**(1/2))/(2*a)
        root2 = (-1*b - det**(1/2))/(2*a)
        print(f"There are two roots: x={root1} and x={root2}")
    elif det == 0:
        root = (-1*b)/(2*a)
        print(f"There is one root: x={root}")
    elif det < 0:
        print("No real roots")


num1 = float(input("Enter: "))
num2 = float(input("Enter: "))
num3 = float(input("Enter: "))

numRoot(num1,num2,num3)



#############
# Factorial #
#############
        

def factorial(a):
    result = 1
    for i in range(1,a+1):
        result = result * i
    
    return result

answer = factorial(5)

print(f"The answer is {answer}")
    