from datetime import date
from abc import ABC, abstractmethod

# ====== Target Interface ======
class IEmployee(ABC):
    @abstractmethod
    def get_info(self):
        pass

# ====== Adaptee (Existing Employee Classes) ======
class Employee:
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date):
        self.name = name
        self.position = position
        self.year_hired = year_hired
        self.salary = salary
        self.hire_date = hire_date

    def get_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, position, year_hired, salary, hire_date, department, team):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.department = department
        self.team = team

class Engineer(Employee):
    def __init__(self, name, position, year_hired, salary, hire_date, expertise, certifications):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.expertise = expertise
        self.certifications = certifications

class Intern(Employee):
    def __init__(self, name, position, year_hired, salary, hire_date, duration, mentor):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.duration = duration
        self.mentor = mentor

# ====== Adapter ======
class EmployeeAdapter(IEmployee):
    def __init__(self, employee: Employee):
        self.employee = employee
    
    def get_info(self):
        info = f"Employee: {self.employee.name}, Position: {self.employee.position} (Hired: {self.employee.year_hired})\n"
        info += f"Salary: ${self.employee.salary}\nHire Date: {self.employee.hire_date}\nAnnual Salary: ${self.employee.get_annual_salary()}\n"
        
        if isinstance(self.employee, Manager):
            info += f"Department: {self.employee.department}\nTeam Members: {self.employee.team}\n"
        elif isinstance(self.employee, Engineer):
            info += f"Expertise: {self.employee.expertise}\nCertifications: {', '.join(self.employee.certifications)}\n"
        elif isinstance(self.employee, Intern):
            info += f"Internship Duration: {self.employee.duration} months\nMentor: {self.employee.mentor}\n"
        
        return info

# ====== CRUD Functions ======
employees = []

def create_employee():
    emp_type = input("Enter Employee Type (Manager/Engineer/Intern): ").strip().lower()
    name = input("Enter Employee Name: ")
    position = input("Enter Position: ")
    year_hired = int(input("Enter Year Hired: "))
    salary = float(input("Enter Salary: "))
    hire_date = date.fromisoformat(input("Enter Hire Date (YYYY-MM-DD): "))
    
    if emp_type == "manager":
        department = input("Enter Department: ")
        team_size = int(input("Enter Number of Team Members: "))
        team = {input("Enter Team Member Name: "): input("Enter Team Member Role: ") for _ in range(team_size)}
        employee = Manager(name, position, year_hired, salary, hire_date, department, team)
    elif emp_type == "engineer":
        expertise = input("Enter Expertise: ")
        certifications = input("Enter Certifications (comma separated): ").split(', ')
        employee = Engineer(name, position, year_hired, salary, hire_date, expertise, certifications)
    elif emp_type == "intern":
        duration = int(input("Enter Internship Duration (months): "))
        mentor = input("Enter Mentor Name: ")
        employee = Intern(name, position, year_hired, salary, hire_date, duration, mentor)
    else:
        print("Invalid employee type!")
        return
    
    employees.append(EmployeeAdapter(employee))
    print("Employee added successfully!")

def read_employees():
    if not employees:
        print("No employees found.")
        return
    
    for idx, emp in enumerate(employees, start=1):
        print(f"ID: {idx}")
        print(emp.get_info())
        print("----------------------")

def update_employee():
    read_employees()
    if not employees:
        return

    emp_id = int(input("Enter Employee ID to update: ")) - 1
    if emp_id < 0 or emp_id >= len(employees):
        print("Invalid Employee ID!")
        return

    employee = employees[emp_id].employee  # Get the actual Employee object
    
    print("\nUpdating Employee Information:")
    employee.name = input(f"Enter new name ({employee.name}): ") or employee.name
    employee.position = input(f"Enter new position ({employee.position}): ") or employee.position
    employee.salary = float(input(f"Enter new salary ({employee.salary}): ") or employee.salary)
    employee.hire_date = date.fromisoformat(input(f"Enter new hire date ({employee.hire_date}): ") or str(employee.hire_date))
    
    print("Employee updated successfully!")

def delete_employee():
    read_employees()
    if not employees:
        return

    emp_id = int(input("Enter Employee ID to delete: ")) - 1
    if emp_id < 0 or emp_id >= len(employees):
        print("Invalid Employee ID!")
        return

    employees.pop(emp_id)
    print("Employee deleted successfully!")

# ====== Main Program ======
if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
