import random

count = 0
randomNum = random.randint(1,100)

while True:
    print("*You will guess a random number from 1 to 100.")
    userNum = int(input("Enter your guess: "))

    if (userNum > randomNum):
        print("Too high\n")
        count += 1
    elif (userNum < randomNum):
        print("Too short\n")
        count += 1
    elif (userNum == randomNum):
        count += 1
        print(f"You successfully guessed the number {randomNum}\n"+
            f"{count} guesses are made")
        break