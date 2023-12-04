# fleet mane holo sarok pothe bimaner shoya like , emad paribahan , shohag poribahan
class Company:
    def __init__(self,name,address,founder) -> None:
        self.name = name
        self.address = address
        self.founder = founder
        self.driver = []
        self.supervisor = []
        self.counter = []
        self.route = []

class Driver:
    def __init__(self,name,age,licence) -> None:
        self.name = name
        self.age = age
        self.licence = licence

class Supervisor:
    def __init__(self,name,age,salary,licence) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.licence = licence
