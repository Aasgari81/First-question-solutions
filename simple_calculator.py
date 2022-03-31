
class Calculator:

    def number_checker(number):

        if not isinstance(number, int) and not isinstance(number, float):
            raise TypeError("Number must be integer or float")
        else:
            return None

    def add (self, first_number, second_number):
        Calculator.number_checker(first_number)
        Calculator.number_checker(second_number)
        return first_number + second_number
    
    def subtract (self, first_number, second_number):
        Calculator.number_checker(first_number)
        Calculator.number_checker(second_number)
        return first_number - second_number
    
    def multiply (self, first_number, second_number):
        Calculator.number_checker(first_number)
        Calculator.number_checker(second_number)
        return first_number * second_number
    
    def divide (self, first_number, second_number):
        Calculator.number_checker(first_number)
        Calculator.number_checker(second_number)
        try:
            result = first_number/second_number
            return result
        except ZeroDivisionError:
            print('Second number can not be zero')
            return 
calculator = Calculator()
print(calculator.divide(25, 0))


