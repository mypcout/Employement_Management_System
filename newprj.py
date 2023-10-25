class Employee:
    def __init__(self, emp_id, name, salary, age, gender, address, city, dob, doi, department, designation, pan, aadhar):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city
        self.dob = dob
        self.doi = doi
        self.department = department
        self.designation = designation
        self.pan = pan
        self.aadhar = aadhar
employee_records = []

while True:
    print("Choose an option:")
    print("1. Add a record of Employee")
    print("2. Delete a record of Employee")
    print("3. Update Employee Details")
    print("4. Search details of Employee")
    print("5. Display Employee with the highest salary")
    print("6. Display Employee with the lowest salary")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add a record of Employee
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))
        age = int(input("Age: "))
        gender = input("Gender: ")
        address = input("Address: ")
        city = input("City: ")
        dob = input("Date of Birth: ")
        doi = input("Date of Joining: ")
        department = input("Department Name: ")
        designation = input("Designation: ")
        pan = input("PAN Card Number: ")
        aadhar = input("Aadhar Number: ")

        new_employee = Employee(emp_id, name, salary, age, gender, address, city, dob, doi, department, designation, pan, aadhar)
        employee_records.append(new_employee)
        print("Employee record added successfully.")

    elif choice == 2:
        # Delete a record of Employee by Employee ID
        emp_id = input("Enter Employee ID to delete: ")
        for employee in employee_records:
            if employee.emp_id == emp_id:
                employee_records.remove(employee)
                print("Employee record deleted successfully.")
                break
        else:
            print("Employee with ID not found.")

    elif choice == 3:
        # Update Employee Details
        sub_choice = int(input("Choose what to update:\n1. Name\n2. Address\n3. DOB\n4. Salary\n0. Back\nEnter sub-choice: "))
        if sub_choice == 1:
            # Update name of Employee
            emp_id = input("Enter Employee ID: ")
            new_name = input("Enter new name: ")
            for employee in employee_records:
                if employee.emp_id == emp_id:
                    employee.name = new_name
                    print("Employee name updated successfully.")
                    break
            else:
                print("Employee with ID not found.")

    elif choice == 4:
        # Search details of Employee
        sub_choice = int(input("Search by:\n1. Employee ID\n2. Employee Name\n3. Department Name\n0. Back\nEnter sub-choice: "))
        if sub_choice == 1:
            emp_id = input("Enter Employee ID: ")
            for employee in employee_records:
                if employee.emp_id == emp_id:
                    print("Employee Found:")
                    break
            else:
                print("Employee with ID not found.")

    elif choice == 5:
        # Display Employee with the highest salary
        if employee_records:
            highest_salary_employee = max(employee_records, key=lambda x: x.salary)
            print("Employee with the highest salary:")
            # Print employee details
        else:
            print("No employee records to display.")

    elif choice == 6:
        # Display Employee with the lowest salary
        if employee_records:
            lowest_salary_employee = min(employee_records, key=lambda x: x.salary)
            print("Employee with the lowest salary:")
        else:
            print("No employee records to display.")

    elif choice == 0:
        print("GoBack!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")