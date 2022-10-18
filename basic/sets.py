list =[7,7,6,5,4,3,2]
mySet = set(list)
print(mySet)

for item in mySet:
    print(item)


# seti=[7,6,5,4,7]
# Set=set(seti)
# print(Set)

# Set=[5,7,5,4,3]
# print(Set)

# mySet.add(7,6,5)
# print(mySet)

mySet.add(10)
mySet.update({5,4,4,3,2,6})
print(mySet)