character=input("Enter your Sentence: ").lower()
vowel_count=0
consonant_count=0
for ch in character:
    if ch in "aeiou":
        vowel_count+=1
    else:
        consonant_count+=1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
