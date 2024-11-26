stack = []  # an empty stack

while True:
    print("1 Push")
    print("2 Pop")
    print("3 Peek")
    print("4 Display")
    print("5 Exit")
    choice = int(input("select action : "))

    if choice == 1:  # push
        item = int(input("push: "))
        stack.append(item)
        print(f"{item} pushed to stack\n")
    elif choice == 2:  # pop
        if len(stack) == 0:
            print("stack is empty")
        else:
            popped_item = stack.pop()
            print(f"popped : {popped_item}")
    elif choice == 3:  # peek
        if len(stack) == 0:
            print("stack is empty")
        else:
            print(f"top : {stack[-1]}")
    elif choice == 4:  # display
        if len(stack) == 0:
            print("stack is empty")
        else:
            print("stack contents :", stack)
    elif choice == 5:  # exit
        print("system close")
        break
    else:
        print("invalid error")
