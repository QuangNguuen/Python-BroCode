print("Enter your pressure in atm: ")
pressure = float(input())

print("  Convert table:   \n" + "1. Convert to kPa\n" + "2. Convert to PSI\n" + "3. Convert to mmHg")
choice = int(input())

if (choice == 1 ):
    pressure = pressure * 101.352
    print("The pressure is", pressure, "kPa")
elif (choice == 2):
    pressure = pressure * 14.6959
    print("The pressure is", pressure, "PSI")
elif (choice == 3):
    pressure = pressure * 760
    print("The pressure is", pressure, "mmHg")
else:
    print("Invalid input. Run again")
