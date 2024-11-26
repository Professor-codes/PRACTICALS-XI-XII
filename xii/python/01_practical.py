number_1 = float(input("Enter number 1 : "))
number_2 = float(input("Enter number 2 : "))
operation = ['+', '-', '*', '/']
print(operation)
op = input("Select operation : ")
0
if op == '+':
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
elif op == '-':
    if number_1 > number_2:
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
    else:
        print(f"{number_2} - {number_1} = {number_2 - number_1}")
elif op == '*':
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
elif op == '/':
    if number_2 == 0:
        print(f"cannot divide by zero")
    else:
        print(f"{number_1} / {number_2} = {number_1 / number_2}")
else:
    print(f"Invalid input")
