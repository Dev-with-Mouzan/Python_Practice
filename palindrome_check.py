def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase for better check
    # But simple requirements usually just mean the string itself
    clean_s = ''.join(e for e in s if e.isalnum()).lower()
    return clean_s == clean_s[::-1]

if __name__ == "__main__":
    val = input("Enter a number or string: ")
    if is_palindrome(val):
        print(f"'{val}' is a palindrome.")
    else:
        print(f"'{val}' is not a palindrome.")
