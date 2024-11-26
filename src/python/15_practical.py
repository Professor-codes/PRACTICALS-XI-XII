word = input("word: ").lower()  # lowercase
vowels = "aeiou"
stack = []  # store vowels

for char in word:
    if char in vowels and char not in stack:
        stack.append(char)  # add unique vowels in stack

if stack:
    print("unique vowels")
    while stack:  # pop and display vowels
        print(stack.pop())  # stack order
else:
    print("No vowels found in the word.")
