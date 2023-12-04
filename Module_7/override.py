class Person:
    def __init__(self,name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat, mas, magso, etc kahi')

    def exersice(self):
        raise NotImplementedError

    
class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # override korce parent class ke
    def eat(self):
        print('Vagetarian!')

    def exersice(self):
        print('Gym a giya taka diye gham jhorai amra!')

    # plus + sign oparator overload 
    def __add__(self,other):
        return self.age + other.age
    
    # multiple * sign oparator overload
    def __mul__(self,other):
        return self.weight * other.weight
    
    # gater than sign oparator overload
    def __gt__(self,other):
        return self.age > other.age
    
    # len oparator 
    def __len__(self):
        return self.name


tamim = Crickter('Tamim Iqbal', 34, 70, 76, 'BD')
riyad = Crickter('Mahmudullah Riyad', 39, 85, 87, 'BD')
# tamim.eat()
# tamim.exersice()

# riyad.eat()
# riyad.exersice()

print(55 + 87)
print('tamim' + 'riyad')
print(tamim + riyad)
print(tamim * riyad)
print(riyad > tamim)
# print(len(riyad))