from datetime import date
from abc import ABC, abstractmethod

# ====== Strategy Interface ======
class EmployeeStrategy(ABC):
    @abstractmethod
    def get_info(self, employee):
        pass

# ====== Concrete Strategies ======
class ManagerStrategy(EmployeeStrategy):
    def get_info(self, employee):
        return (f"Employee: {employee.name}, Position: {employee.position} (Hired: {employee.year_hired})\n"
                f"Salary: ${employee.salary}\nHire Date: {employee.hire_date}\nAnnual Salary: ${employee.get_annual_salary()}\n"
                f"Department: {employee.department}\nTeam Members: {employee.team}\n")

class EngineerStrategy(EmployeeStrategy):
    def get_info(self, employee):
        return (f"Employee: {employee.name}, Position: {employee.position} (Hired: {employee.year_hired})\n"
                f"Salary: ${employee.salary}\nHire Date: {employee.hire_date}\nAnnual Salary: ${employee.get_annual_salary()}\n"
                f"Expertise: {employee.expertise}\nCertifications: {', '.join(employee.certifications)}\n")

class InternStrategy(EmployeeStrategy):
    def get_info(self, employee):
        return (f"Employee: {employee.name}, Position: {employee.position} (Hired: {employee.year_hired})\n"
                f"Salary: ${employee.salary}\nHire Date: {employee.hire_date}\nAnnual Salary: ${employee.get_annual_salary()}\n"
                f"Internship Duration: {employee.duration} months\nMentor: {employee.mentor}\n")

# ====== Context Class ======
class EmployeeContext:
    def __init__(self, employee, strategy: EmployeeStrategy):
        self.employee = employee
        self.strategy = strategy
    
    def set_strategy(self, strategy: EmployeeStrategy):
        self.strategy = strategy
    
    def get_employee_info(self):
        return self.strategy.get_info(self.employee)

# ====== Employee Classes (Unchanged) ======
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
        strategy = ManagerStrategy()
    elif emp_type == "engineer":
        expertise = input("Enter Expertise: ")
        certifications = input("Enter Certifications (comma separated): ").split(', ')
        employee = Engineer(name, position, year_hired, salary, hire_date, expertise, certifications)
        strategy = EngineerStrategy()
    elif emp_type == "intern":
        duration = int(input("Enter Internship Duration (months): "))
        mentor = input("Enter Mentor Name: ")
        employee = Intern(name, position, year_hired, salary, hire_date, duration, mentor)
        strategy = InternStrategy()
    else:
        print("Invalid employee type!")
        return
    
    employees.append(EmployeeContext(employee, strategy))
    print("Employee added successfully!")

def read_employees():
    if not employees:
        print("No employees found.")
    for emp in employees:
        print(emp.get_employee_info())
        print("----------------------")

# ====== Main Program ======
if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
