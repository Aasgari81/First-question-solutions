from inspect import FullArgSpec


class Employee:
    def __init__ (self, fullname, **kwargs):
        if not isinstance(fullname, str):
            raise TypeError("Name should be string")
        first_name, last_name = fullname.split(sep = " ")
        self.firstname = first_name
        self.lastname = last_name
        self.__dict__.update(kwargs)
mary = Employee("Mary Major", salary=120000)
print(mary.salary)

