def isPalindrome(s):
	return s == s[::-1]

s = input("Enter a string\n")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")