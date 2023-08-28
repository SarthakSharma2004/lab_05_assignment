class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display(self):
        print("Employee ID\tName\tAge\tSalary (PM)")
        print("-----------------------------------")
        for emp in self.employees:
            print(emp)

if __name__ == "__main__":
    db = EmployeeDatabase()

    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input())

    if choice == 1:
        db.sort_by_age()
    elif choice == 2:
        db.sort_by_name()
    elif choice == 3:
        db.sort_by_salary()
    else:
        print("Invalid choice!")

    db.display()
