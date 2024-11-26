with open("integers.bin", "wb") as binary_file:
    n = int(input("Number of integers to store : "))
    print("Integers : ")
    for _ in range(n):
        num = int(input())  # integer input
        binary_file.write(num.to_bytes(4))  # convert to binary and write

print("stored successfully.\n")

# read and display
with open("integers.bin", "rb") as binary_file:
    print("Reading integers :")
    while True:
        data = binary_file.read(4)  # 4 bytes
        if not data:
            break  # stop reading
        num = int.from_bytes(data)  # convert binary to integer
        print(num, end=" ")
print()
