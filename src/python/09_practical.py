with open("source.txt", "w") as source_file:
    source_file.write(input("Write text here: "))

# open source file for reading
with open("source.txt", "r") as source_file:
    content = source_file.read()

# open destination file for writing
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)

print("copied successfully!")
