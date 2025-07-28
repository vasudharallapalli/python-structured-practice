
# word = list(input("Enter a string: "))
# !!! need not convert to list, as string is iterable

# for _ in range(0, len(word)):
#     if word[_] == word[len(word) - 1 - _]:
#         print(f"{word[_]} is a palindrome character at position {_}")
#     else:
#         print(f"{word[_]} is not a palindrome character at position {_}")

word = input("Enter a string: ")

if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
