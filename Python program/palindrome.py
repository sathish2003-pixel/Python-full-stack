val = input("Enter the str:")
rev = ""
for i in val:
    rev = i + rev # This line correctly appends each character to the beginning of rev, effectively reversing the string
if rev == val:
    print(val, "is a palindrome")
else:
    print(val, "is not a palindrome")