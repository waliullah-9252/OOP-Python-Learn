from abc import ABC, abstractmethod
# abstract base class
class Animal(ABC):
    @abstractmethod  # enforce all drived class to have eat method
    def eat(self):
        print('I need Food')

    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name = name
        self.catagory = 'Monkey'
        super().__init__()

    def eat(self):
        print('Hey na na nana ! , eating banana')

    def move(self):
        print('Hangging this system now')

lyka = Monkey('Lyka')
lyka.eat()