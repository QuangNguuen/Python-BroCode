total = 1
num = int(input("Enter a number: "))
original_num = num


if num == 0:
    print("Your factorial is 1")
    total = 1
elif num < 0:
    print("Invalid values. Please try again")
    total = None

while num > 1:
    
    total = total * num
    num = num - 1


print(f"{original_num}! is", total)
