class Book:
    def __init__(self,name) -> None:
        self.name = name

    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab = lab
        super().__init__(name)

    def read(self):
        print('Reading the vector chapter now!')

tapon = Physics('Tapon Sir' , True)
print(issubclass(Physics, Book))
print(isinstance(tapon, Physics))
print(isinstance(tapon, Book))

tapon.read()