#Переписать код в соответствии с Single Responsibility Principle

from datetime import date

class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name}, dob - {self.dob}"


class SalaryCalculator:
    def __init__(self, employee):
        self.employee = employee

    def calculate_net_salary(self):
        tax = int(self.employee.base_salary * 0.25)  # рассчитать налог другим способом
        return self.employee.base_salary - tax