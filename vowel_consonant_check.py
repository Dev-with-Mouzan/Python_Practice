def check_vowel_consonant(char):
    if len(char) != 1 or not char.isalpha():
        return "Invalid input. Please enter a single letter."
    
    char = char.lower()
    if char in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

if __name__ == "__main__":
    char = input("Enter a character: ")
    print(f"The character '{char}' is a {check_vowel_consonant(char)}.")
