#Conversion rate between human's and dog's age
HUMAN_TO_DOG = 10.5
HUMAN_TO_DOG_AFTER = 4

#Set the default value for human age
human = 0

#Run the while loop
while True:
    #Take the input fro user
    human = float(input("Enter an age in human years: "))

    #If statement to determine if the age is valid or not
    if (human >= 0):
        if human >= 2:
            remain = human - 2
            dog = 2 * HUMAN_TO_DOG + remain * HUMAN_TO_DOG_AFTER

            print(f"That's equivalent to {dog} dog years")
        else:
            dog = human * HUMAN_TO_DOG

            print(f"That's equivalent to {dog} dog years")
    else:
        break