class Calculator:
    brand = 'Casio MS-999es'
    color = 'Black'
    price = 2200

    def add(self,num1,num2):
        summation = num1 + num2
        return summation
    def sub(self,num1,num2):
        subtraction = num1 - num2
        return subtraction
    def multi(self,num1,num2):
        multification = num1 * num2
        return multification
    def divided(self,num1,num2):
        divided = num1 / num2
        return divided
    def reminder(self,num1,num2):
        remainder = num1 % num2
        return remainder


my_calculator = Calculator()
summation = my_calculator.add(23,25)
subtraction = my_calculator.sub(45, 24)
multification = my_calculator.multi(12, 8)
divided = my_calculator.divided(45, 5)
remainder = my_calculator.reminder(45, 22)
print(summation)
print(subtraction)
print(multification)
print(divided)
print(remainder)