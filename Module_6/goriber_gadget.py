class Laptop:
    def __init__(self,brand,price,color,ssd,memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.ssd = ssd
        self.memory = memory

    def run(self):
        return f'Running this {self.brand} Laptop'
    
class Phone:
    def __init__(self,brand,price,color,features,camera) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.features = features
        self.camera = camera

    def run(self):
        return f'Running this {self.brand} Phone'
    
    def phone_call_and_sms(self,number,sms):
        return f'Calling karim {number} and text is : {sms}'
    

class Camera:
    def __init__(self,brand,price,color,lens,pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.lens = lens
        self.pixel = pixel

    def run(self):
        return f'Running this {self.brand} camera'
    
