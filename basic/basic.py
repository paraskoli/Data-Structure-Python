#taking input from user
Birth_Year=int(input("Enter your Birth Year: "))
print(2022-Birth_Year)

#Sum of two number
first=int(input("Enter a Number:"))
second=int(input("Enter a Number:"))
print(first+second)

#multi line input
name="""paras 
        koli """
print(name.upper())
print(name.capitalize())
print(name.lower())
print(name)
print(name[2:])
print(name[-1])

name=("paraskoli1")
print(name[-8:])
print(name[-1])
print(name[2:5])
print(name.find("k"))
print(name.replace("koli","kumar"))
print(name.isalnum()) #both alphabet and number
print(name.isalpha()) #only alphabet
print(name.isnumeric()) #only number