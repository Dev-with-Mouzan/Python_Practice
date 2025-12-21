text = input("Enter a string: ").lower()
vowel="aeiou"
count=0
for t in text:
    if t in vowel:
        count+=1



print(f"Number of vowels: {count}")
