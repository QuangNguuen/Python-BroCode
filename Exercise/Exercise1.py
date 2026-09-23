#Constant to convert from human to dog age
HUMAN_TO_DOG = 7

#While loop, run until the loop breaks
while True:
    #Create a list for user to choose want task to run
    choose = int(input("1. Convert age\n" + "2. Quit\n" + "Enter your input here: "))

    #If user choose 1, then run the age converter from human to dog
    if choose == 1:
        name = input("Enter a human name: ")
        age = float(input("Enter a human age: "))

        dog_age = age * HUMAN_TO_DOG
        print(f"I can't believe that {name} is {age} years old! That's {dog_age} years old in dog years!\n")

    #If user chooses 2, break the loop and stop the program
    elif choose == 2:
        break

    #Catch any errors if the input is larger than 2
    else:
        print("Invalid input. Please try again")