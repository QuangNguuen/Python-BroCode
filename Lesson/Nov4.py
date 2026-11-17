line = input("Enter a number, Q to quit: ")
values=[]

while line != "":
    values.append(float(line))

    line = input("Enter a number, Q to quit: ")


values.sort()
print(values)

if len(values) % 2 == 1:
    index = len(values)//2
    print(values[index])
else:
    sum = (values[len(values)//2] + values[len(values)//2-1])/2
    print(sum)