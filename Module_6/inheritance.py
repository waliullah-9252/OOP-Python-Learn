# base class , parent class , common attribute + functionality class
# derived class , child class , uncommon attribute + functionality class

class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running this {self.brand} Laptop'


class Laptop(Gadget):
    # def __init__(self,ssd,memory) -> None:
    #     self.ssd = ssd
    #     self.memory = memory
    def __init__(self,ssd,memory, brand, price, color, origin) -> None:
        self.ssd = ssd
        self.memory = memory
        super().__init__(brand, price, color, origin)
    
    
class Phone(Gadget):
    # def __init__(self,features,camera) -> None:
    #     self.features = features
    #     self.camera = camera

    def __init__(self,features,camera, brand, price, color, origin) -> None:
        self.features = features
        self.camera = camera
        super().__init__(brand, price, color, origin)
    
    def phone_call_and_sms(self,number,sms):
        return f'Calling karim {number} and text is : {sms}'
    

class Camera(Gadget):
    # def __init__(self,lens,pixel) -> None:
    #     self.lens = lens
    #     self.pixel = pixel

    def __init__(self, brand, price, color, origin,pixel,lens) -> None:
        self.pixel = pixel
        self.lens = lens
        super().__init__(brand, price, color, origin)

    def __repr__(self) -> str:
        return f'Camera name: {self.brand}. Price: {self.price}. Color: {self.color}. Origin: {self.origin}. Pixel: {self.pixel}. Lens: {self.lens}'
        return super().__repr__()


my_camera = Camera('Cannon', 22300, 'black', 'China', '50 mega pixel', 'Zoom Lens')
print(my_camera)
    
