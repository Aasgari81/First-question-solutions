class Employee:
    def __init__ (self, first_name, last_name):
        if not isinstance(first_name, str) and not isinstance(last_name, str):
            raise TypeError("Name must be string")
        if not first_name.strip() or not last_name.strip():
            raise ValueError("None is not acceptable")
        self.fullname = f'{first_name} {last_name}'
        self.email = f'{first_name}.{last_name}@company.com'
emp_1 = Employee("John", None)