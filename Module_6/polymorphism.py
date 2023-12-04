# poly --> many (multiple)
#morph --> sahpe

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('mew , mew !')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('ghew ghew!')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Waka Waka Waka')
    

don = Cat('Me ho Don')
don.make_sound()

shaphard = Dog('Jarman Shaphard')
shaphard.make_sound()

messi = Goat('Leonel Messi')
messi.make_sound()

neymer = Goat('Neymar Joniur')
neymer.make_sound()

alll = [don,shaphard,messi,neymer]
for al in alll:
    al.make_sound()