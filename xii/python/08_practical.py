with open("numbers.txt", "w") as file:
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    file.write(f"{num1}\n{num2}")

addition = num1 + num2

with open("result.txt", "w") as file:
    file.write(f"Addition of {num1} and {num2} = {addition}")

print(f"Addition of {num1} and {num2} = {addition}")
