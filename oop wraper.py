print("===== EMPLOYEE MANAGEMENT SYSTEM =====")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        super().show_details()
        print("Employee ID:", self.emp_id)
        print("Salary: Rs.", f"{self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print("Department:", self.department)


persons = []
employees = []
managers = []


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0:
                return age
            print("Age must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_salary():
    while True:
        try:
            salary = float(input("Enter salary: Rs. "))
            if salary >= 0:
                return salary
            print("Salary cannot be negative.")
        except ValueError:
            print("Please enter a valid salary.")


def get_employee_id():
    while True:
        emp_id = input("Enter Employee ID: ").strip()

        if not emp_id:
            print("Employee ID cannot be empty.")
        elif any(
            item.emp_id.lower() == emp_id.lower()
            for item in employees + managers
        ):
            print("This Employee ID already exists.")
        else:
            return emp_id


def create_person():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = get_age()
    person = Person(name, age)
    persons.append(person)

    print("Person created successfully!")


def create_employee():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = get_age()
    emp_id = get_employee_id()
    salary = get_salary()

    employee = Employee(name, age, emp_id, salary)
    employees.append(employee)

    print("Employee created successfully!")


def create_manager():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = get_age()
    emp_id = get_employee_id()
    salary = get_salary()
    department = input("Enter department: ").strip()

    if not department:
        print("Department cannot be empty.")
        return

    manager = Manager(name, age, emp_id, salary, department)
    managers.append(manager)

    print("Manager created successfully!")


def show_people():
    if not persons:
        print("No persons found.")
        return

    for number, person in enumerate(persons, start=1):
        print("\nPerson", number)
        person.show_details()


def show_employees():
    if not employees:
        print("No employees found.")
        return

    for number, employee in enumerate(employees, start=1):
        print("\nEmployee", number)
        employee.show_details()


def show_managers():
    if not managers:
        print("No managers found.")
        return

    for number, manager in enumerate(managers, start=1):
        print("\nManager", number)
        manager.show_details()


while True:
    print("\n----- MAIN MENU -----")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number from 1 to 5.")
        continue

    if choice == 1:
        create_person()

    elif choice == 2:
        create_employee()

    elif choice == 3:
        create_manager()

    elif choice == 4:
        print("\n----- SHOW DETAILS -----")
        print("1. Persons")
        print("2. Employees")
        print("3. Managers")
        print("4. All Employees and Managers")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            show_people()

        elif option == 2:
            show_employees()

        elif option == 3:
            show_managers()

        elif option == 4:
            show_employees()
            show_managers()

        else:
            print("Invalid option!")

    elif choice == 5:
        print("Exiting Employee Management System.")
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
