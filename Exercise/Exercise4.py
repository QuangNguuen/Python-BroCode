#Define the int2ordinal function
def int2ordinal(number):
    #Any numbers that are 11,12,13 or end with 11,12,13 go with the th suffix
    if number%100 in (11,12,13):
        return(str(number)+"th")
    elif number%10==1 or number%100==1:
        return(str(number)+"st")
    elif number%10==2 or number%100==2:
        return(str(number)+"nd")
    elif number%10==3 or number%100==3:
        return(str(number)+"rd")
    else:
        return(str(number)+"th")

#Define the main function
def main():
    #User input
    day = int(input("Enter a day between 1 and 31: "))
    month = int(input("Enter a month between 1 and 12: "))
    year = int(input("Enter a year between 1 and 2100: "))

    #Output
    print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
        "month of the", int2ordinal(year), "year, something amazing happened!")

#Call the function
main()

