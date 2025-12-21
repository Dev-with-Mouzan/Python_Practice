val = input("Enter a number or string: ")
if val == val[::-1]:
        print(f"'{val}' is a palindrome.")
else:
        print(f"'{val}' is not a palindrome.")
