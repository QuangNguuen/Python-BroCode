def int2ordinal(number):
    digit = []
    for char in str(number):
        digit.append(char)
    if (digit[len(digit-2)]+digit[len(digit-1)])  == "01":
        return(f'{number}+st')
    elif (digit[len(digit-2)]+digit[len(digit-1)])  == "02":
        return(f'{number}+nd')
    elif (digit[len(digit-2)]+digit[len(digit-1)])  == "03":
        return(f'{number}+rd')
    else:
        return(f'{number}+th')

def main():
    day = int(input("Enter a day between 1 and 31: "))
    month = int(input("Enter a month between 1 and 12: "))
    year = int(input("Enter a year between 1 and 2100: "))

    print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
        "month of the", int2ordinal(year), "year, something amazing happened!")
main()

