total = 1


number = int(input("Enter a number: "))

if number > 0:
    for i in range (1,number+1):
        total = total * i
    print(f"The factorial is: {total}")
elif number == 0:
    total = 1
    print(f"The factorial is: {total}")
else:
    print("Invalid input")
