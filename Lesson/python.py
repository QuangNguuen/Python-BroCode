count = 0
total = 0
line = input("Enter one integer (Blank to exit): ")

while line != "":
    num = float(line)

    count = count + 1
    total = total + num

    line = input("Enter one integer (Blank to exit): ")

if count > 0:
    print("The average is", total/count)
else:
    print("Cannot to computed")

    