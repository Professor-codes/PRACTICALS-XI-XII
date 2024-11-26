num = int(input("numbers in tuple: "))
tpl_element = []

# input elements
for _ in range(num):
    element = int(input(f"Enter number {_}: "))
    tpl_element.append(element)

def count_even_odd(numbers):
    even, odd = 0, 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

even, odd = count_even_odd(tpl_element)

print(f"\ntuple{tpl_element}")
print(f"even -> {even}")
print(f"odd -> {odd}")
