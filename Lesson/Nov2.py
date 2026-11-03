name = [1,2,3]
name.append(4)
print(name)


name_1 = [1,2,3,4]
name_1.insert(2,"Hello")
print(name_1)


name_2 = [1,2,3,4,5]
name_2.insert(len(name_2),6)
print(name_2)


name_3 = [0]
if 0 in name_3:
    print("True")
else:
    print("False")


values = [1,2,1,3,4,2,1,1,1,5]
values.remove(5)
print(values)

while 1 in values:
    values.remove(1)
print(values)