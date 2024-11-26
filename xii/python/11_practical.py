import pickle  # handle binary data

# Open the binary file for writing
with open("student.txt", "wb") as binary_file:
    n = int(input("Number of student records you want to add: "))
    for _ in range(n):
        name = input(f"Student {_ + 1} name: ")
        marks = int(input(f"Student {_ + 1} marks: "))
        record = {"name": name, "marks": marks}  # Create a dictionary for each student
        pickle.dump(record, binary_file)  # Write the record to the file
    # Add a sentinel value at the end of the file
    pickle.dump(None, binary_file)

print("Saved successfully.")

# Open the binary file for reading
with open("student.txt", "rb") as binary_file:
    print("Reading records from the binary file:")
    while True:
        record = pickle.load(binary_file)  # Deserialize the record from the file
        if record is None:  # Check for the sentinel value
            break
        print(f'Name: {record["name"]}, Marks: {record["marks"]}')
