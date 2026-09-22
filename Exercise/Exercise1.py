#Constants for age's converter
DOG_TO_HUMAN = 7
HUMAN_TO_DOG = 1/7

while True:
    #Give user the list of choices in the program
    #The program runs until the user break the while loop, by selecting 3 to quit
    print("1. Human's age to dog's age\n" + "2. Dog's age to human's age\n" + "3. Exit")
    choose = int(input("Enter your choice here: "))

    #If user chooses 1, then convert human's to dog's age
    if choose == 1:
        name = input("Enter a human name: ")
        age = float(input("Enter a human age: "))

        dog_age = age * HUMAN_TO_DOG
        dog_age = round(dog_age,2) #Round the age to 2 decimals place if the value returns too long in decimal places
        print(f"I can't believe that {name} is {age} years old! That's {dog_age} years old in dog years!\n")

    #If user chooses 2, then convert dog's to human's age
    elif choose == 2:
        name = input("Enter a dog name: ")
        age = float(input("Enter a dog age: "))

        human_age = age * DOG_TO_HUMAN
        print(f"I can't believe that {name} is {age} years old! That's {human_age} years old in human years!\n")

    #If user chooses 3, break the loop and stop the program
    elif choose == 3:
        break

    #Catch any invalid input, in case the inputs are not 1, 2, or 3
    else:
        print("Invalid input. Please try again\n")