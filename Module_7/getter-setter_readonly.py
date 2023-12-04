# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.

class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter readonly attribute
    @property
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    

    # setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            return 'Salary can not be neagative!'
        else:
            self.__money += value


samsu = User('Samsu Ostad', 22, 30000)
# print(samsu.__money)
# print(samsu._age)
# print(samsu.age())
print(samsu.age)
print(samsu.salary)
samsu.salary = 5000
print(samsu.salary)