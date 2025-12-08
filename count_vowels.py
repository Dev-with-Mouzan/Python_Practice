def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Number of vowels: {count_vowels(text)}")
