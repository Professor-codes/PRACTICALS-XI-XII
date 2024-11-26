number = int(input("number : "))

# initialize
fib = (0,)  # first fibonacci number
a, b = 0, 1  # initialize first two fibonacci numbers

print(fib)

for _ in range(1, number):
    fib += (b,)  # append next fib number to tuple
    a, b = b, a + b  # update the fib numbers
    print(fib)
