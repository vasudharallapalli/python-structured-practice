# Count vowels and consonants in a string
vowel = 0
consonant = 0

def count_vowels_and_consonants(text:str) -> tuple[int, int]:
    """Counts the number of vowels and consonants in a given string."""
    global vowel, consonant
    #The global keyword is used inside a function to tell Python that you want to use the global variables (declared outside the function), rather than creating new local ones.
    for char in text:
        if char.isalpha():
            if char in "aeiouAEIOU":
                vowel += 1
            else:
                consonant += 1
    return vowel, consonant

input_list = list(input("Enter a string: "))
vowel, consonant = count_vowels_and_consonants(input_list)  
print(f"Total number of vowels and consonants in the string are: {vowel} and {consonant} respectively.")


