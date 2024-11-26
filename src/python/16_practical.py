employee_stack = []

while True:
    print("add")
    print("delete")
    print("view")
    print("exit")
    choice = input("select action: ")

    if choice == 'add':
        emp_id = input("Enter Id: ")
        emp_name = input("Enter Name: ")
        emp_department = input("Enter Department: ")
        # employee record
        employee = {
            "ID": emp_id,
            "Name": emp_name,
            "Department": emp_department
        }
        # Add the employee
        employee_stack.append(employee)
        print("Added successfully.\n")

    elif choice == 'delete':
        if not employee_stack:
            print("No employees to delete!\n")
        else:
            removed_employee = employee_stack.pop()
            print(f"Deleted employee : {removed_employee}\n")

    elif choice == 'view':
        if not employee_stack:
            print("No employees to display!\n")
        else:
            print("Employee records:")
            for emp in reversed(employee_stack):  # stack order
                print(emp)
            print()

    elif choice == '4':
        print("System close!")
        break

    else:
        print("Invalid choice. Please try again!\n")
