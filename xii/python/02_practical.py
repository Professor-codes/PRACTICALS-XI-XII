number = int(input("Enter number : "))
t = "prime"
f = "not a prime"

if number <= 1:
    print(f"{f}")
else:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    print(f"{t if prime else f}")
