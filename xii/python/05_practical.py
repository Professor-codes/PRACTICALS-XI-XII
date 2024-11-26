unsort_list = [5, 2, 4, 1, 3]
list_len = len(unsort_list)  # 5

for i in range(list_len - 1):  # 0 1 2 3
    for j in range(list_len - i - 1):
        if unsort_list[j] > unsort_list[j + 1]:
            unsort_list[j], unsort_list[j + 1] = unsort_list[j + 1], unsort_list[j]

print(unsort_list)

"""
unsort_list[j], unsort_list[j + 1] = unsort_list[j + 1], unsort_list[j]

left
unsort_list[j], unsort_list[j + 1] specifies the two elements in the list that you want to update

right
unsort_list[j + 1], unsort_list[j] specifies the new values for those positions, but in swapped order

a = 5
b = 10
print("a :", a)  # 5
print("b :", b)  # 10

a, b = b, a
print("a :", a)  # 10
print("b :", b)  # 5

"""


