dictionary={"name":"Paras","age":22}
# print(dictionary)
mydict=dictionary.copy()
print(mydict)

print(dictionary.items())
print(dictionary.get("name"))
print(dictionary.values())
print(dictionary.keys())
print(dictionary.update())
print(dictionary.pop("name"))
print(dictionary)

for items in dictionary:
    print(items)

for item in dictionary.values():
    print(item)

dictionary.clear()
print(dictionary)
