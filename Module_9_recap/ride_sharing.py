from abc import ABC,abstractmethod
class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []

    def add_drivers(self,driver):
        self.drivers.append(driver)

    def add_riders(self,rider):
        self.drivers.append(rider)

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.eamil = email
        self.nid = nid

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Drivers(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f'Driver Name: {self.name} and his mail address is : {self.eamil}')

class Riders(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.current_ride = None
    
    def display_profile(self):
        print(f'Rider Name: {self.name} and his mail address is : {self.eamil}')
    
    def ride_request(self,uber,destination):
        if not self.current_ride:
            ob = Ride_Matching(uber.drivers)
            res = ob.has_drivers(self,destination)
            print('Your result is , ', res)
            self.current_ride = res
            return True
        else:
            return False

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.drivers = None
        self.riders = None

    def start_ride(self):
        pass

    def end_ride(self):
        pass

    def __repr__(self) -> str:
        return f'Now I am Riding from {self.start_location} to {self.end_location}'
    
class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.drivers = drivers

    def has_drivers(self,start_rider,destination):
        if len(self.drivers) > 0:
            ride = Ride(start_rider.current_location,destination)
            return ride
        else:
            return 'Sorry, Rider Not found yet'


# using example

# create a ride sharing company
uber = Ride_Sharing('UBER')

# create a driver
rahim = Drivers('Rahim Uddin', 'rahimuddin@gmail.com', 3954954, 'Mirpur 10')
uber.add_drivers(rahim)

# create a rider
karim = Riders('Karim Uddin', 'karimuddin@gamil.com', 30983798, 'Kajipara Metro Station')
uber.add_riders(rahim)

# crate a ride request
if karim.ride_request(uber,'Shewrapara Metro Station'):
    print('Travelling......!')
else:
    print('Not ride yet')