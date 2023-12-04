from abc import ABC,abstractmethod
class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []

    def add_drivers(self,driver):
        self.drivers.append(driver)

    def add_riders(self,rider):
        self.riders.append(rider)


class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Drivers(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver Name: {self.name} and there mail is: {self.email}.')
    
class Riders(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.current_ride = None

    def display_profile(self):
        print(f'Rider Name: {self.name} and there mail is: {self.email}')
    
    def ride_request(self,uber,destination):
        print('Looking here!')
        if not self.current_ride:
            ob = Ride_Matching(uber.drivers)
            res = ob.has_drivers(self,destination)
            print('Your result is, ', res)
            self.current_ride = res
            return True
        else:
            return False
        

class Ride:
    def __init__(self,start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.drivers = None
        self.riders = None
     
    def start_ride(self):
        pass

    def end_ride(self):
        pass

    def __repr__(self) -> str:
        return f'Now I am Riding from {self.start_location} to {self.end_location}.'
    
class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.drivers = drivers

    def has_drivers(self,rider_start,destinatin):
        if len(self.drivers) > 0:
            ride = Ride(rider_start.current_location,destinatin)
            return ride
        else:
            return 'Sorry, driver not avilable now !'


# using example

# createing a riding company
uber = Ride_Sharing('UBER')

# create a derivers
rahim = Drivers('Rahim Uddin', 'rahimuddin@gmail.com', 2342445, 'Azimpur')
uber.add_drivers(rahim)

# create a rider
karim = Riders('Karim Uddin', 'karimuddin@gmail.com', 3754948, 'Khilkhet')
uber.add_riders(karim)

# ride requset 
if karim.ride_request(uber,'Air port'):
    print('Travelling.....')
else:
    print('No ride found !')
