text = input("string : ")
print(text)

i = 0
lowercase = 0
uppercase = 0
lowercase_list = []
uppercase_list = []

for letter in text:
    if letter.islower():
        lowercase = lowercase + 1
        lowercase_list.append(letter)
    if letter.isupper():
        uppercase = uppercase + 1
        uppercase_list.append(letter)

print(f"lowercase count : {lowercase}")
print(f"uppercase count : {uppercase}")

print(f"lowercase letters : {' '.join(lowercase_list)}")
print(f"uppercase letters : {' '.join(uppercase_list)}")
