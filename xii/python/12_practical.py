import csv

# open and read the student.csv file
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))  # print each row, values separated by commas
