class Order:
    def __init__(self,coustomer,items) -> None:
        self.coustomer = coustomer
        self.items = items
        total = 0
        for item in items:
            total += item.price
        self.bill = total