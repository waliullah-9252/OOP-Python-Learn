class Family:
    def __init__(self,address) -> None:
        self.address = address

class School:
    def __init__(self,name) -> None:
        self.name = name

class Sports:
    def __init__(self,game) -> None:
        self.game = game

class Studet(Family,School,Sports):
    def __init__(self, address,name,game) -> None:
        Family.__init__(self,address)
        School.__init__(self,name)
        Sports.__init__(self,game)
        super().__init__(address)
        