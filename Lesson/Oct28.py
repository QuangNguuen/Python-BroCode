import random
def operator():

    opperator = random.randint(0,1)

    if (opperator==0):
        return "+"
    elif (opperator==1):
        return "*"

def math():
    MAX_VALUE = 10
    MIN_VALUE = 1
    firstNum = random.randint(MIN_VALUE,MAX_VALUE)
    secondNum = random.randint(MIN_VALUE,MAX_VALUE)

    op = operator()
    if op == "+":
        answer = firstNum + secondNum
    elif op == "*":
        answer = firstNum * secondNum

    return op, answer, firstNum, secondNum

def question():
    op,answer,firstNum,secondNum = math()
    for i in range(1,11):
        ...

    