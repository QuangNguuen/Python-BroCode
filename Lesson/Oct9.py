total = 1
num = int(input("Enter a number: "))


if num == 0:
    print("Your factorial is 1")
    total = 1
if num < 0:
    print("Invalid values. Please try again")
    total = None

while num > 1:
    
    total = total * num
    num = num - 1


print("Your factorial is", total)
