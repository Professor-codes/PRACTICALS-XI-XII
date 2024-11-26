def count_character(text, letter):
    count = 0
    for i in text:
        if i in letter:
            count += 1
    return count

text = input("text: ")
letter = input("letter: ")
result = count_character(text, letter)
print(f"{letter} count : {result}")
