import csv

# data written in csv file
students = [
    ["Maxim", "98", "male"],
    ["Zia", "81", "female"],
    ["John", "78", "male"],
    ["Tisa", "78", "female"],
]

# write data to student.csv
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("saved student.csv")
