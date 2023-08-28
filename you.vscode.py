class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, emp):
        self.employees.append(emp)
    
    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)
    
    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)
    
    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)
    
    def print_employees(self):
        for emp in self.employees:
            print(emp)
    
if __name__ == "__main__":
    emp_db = EmployeeDatabase()

    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        emp_db.sort_by_age()
    elif choice == 2:
        emp_db.sort_by_name()
    elif choice == 3:
        emp_db.sort_by_salary()
    else:
        print("Invalid choice")
        exit(1)
    
    print("\nSorted Employee Data:")
    emp_db.print_employees()
