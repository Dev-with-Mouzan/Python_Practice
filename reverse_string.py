def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    print(f"Reversed string: {reverse_string(text)}")
