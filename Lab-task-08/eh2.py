class SalaryOutOfRangeError(Exception):
    def __init__(self, message="Salary must be within the range of 20,000 to 60,000."):
        self.message = message
        super().__init__(self.message)

class Employee:
    def __init__(self, name, monthly_salary):
        if 20000 <= monthly_salary <= 60000:
            self.name = name
            self.monthly_salary = monthly_salary
        else:
            raise SalaryOutOfRangeError()

    def display_info(self):
        """Displays the details of the employee."""
        print(f"Employee Name: {self.name}, Monthly Salary: {self.monthly_salary}")

# Handling the creation of an employee and potential exceptions
try:
    employee = Employee("John", 15000)
    employee.display_info()
except SalaryOutOfRangeError as error:
    print(f"Error: {error}")
