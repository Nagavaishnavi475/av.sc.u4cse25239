def employee(emp_list, target, index=0):
    if index == len(emp_list):
        return False
    if emp_list[index] == target:
        return True
    return employee(emp_list, target, index + 1)
employees = [510, 511, 512, 513, 514]
target_id = int(input("Enter Employee ID to search: "))
if employee(employees, target_id):
    print("Employee ID Found.")
else:
    print("Employee ID Not Found.")
