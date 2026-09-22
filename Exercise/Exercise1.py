#Constant to convert from human to dog age
HUMAN_TO_DOG = 7

while True:
    choose = int(input("1. Convert age\n" + "2. Quit\n" + "Enter your input here: "))

    if choose == 1:
        name = input("Enter a human name: ")
        age = float(input("Enter a human age: "))

        dog_age = age * HUMAN_TO_DOG
        print(f"I can't believe that {name} is {age} years old! That's {dog_age} years old in dog years!\n")
    elif choose == 2:
        break
    else:
        print("Invalid input. Please try again")