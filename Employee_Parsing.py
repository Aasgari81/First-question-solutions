class Employee:
    def __init__ (self, first_name, last_name, salary) -> object:
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Name must be string")
        if not isinstance(salary, int) and not isinstance(salary, float):
            raise TypeError("Salary must be integer or float")
        self.firstname = first_name
        self.lastname = last_name
        self.salary = salary

    def from_string(information):
        information = information.strip()
        first_name, last_name, salary = information.split(sep="-")
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Name must be string")
        if not salary.isnumeric():
            raise TypeError("Salary must be integer or float")
        salary = float(salary)
        self = Employee(first_name, last_name, salary)
        return self
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.salary)



        