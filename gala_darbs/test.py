
class ModernHouse():
    # again __init__ is called just after the object is created
    def __init__(self, name="", address="", rooms=4, floors=1):
        self.name = name
        self.address = address
        self.rooms = rooms
        self.floors = floors
        # self.print_address() # no need for this if I can now print
        print(self) # this will print the object (not very useful but possible
    # there are many __dunder__ methods in Python, __init__ is just one of them
    # full list is here: https://docs.python.org/3/reference/datamodel.html#special-method-names
    # one very useful is __str__ that is called when we try to print the object
    def __str__(self):
        # only requirement is that we are returning a string
        # we could prepare the string here main thing that we DO NOT PRINT IT! just return
        return f"ModernHouse object called {self.name} with {self.rooms} rooms and {self.floors} floors"
    
    # i can make my own + for the object using __add__ method
    def __add__(self, other):
        rooms = self.rooms + other.rooms
        floors = self.floors + other.floors
        name = f"{self.name} and {other.name}"
        # we will return a new object of the same class
        return ModernHouse(name=name, rooms=rooms, floors=floors)
    # we can define our own -, *, /, <, >, ==, !=, etc. methods 

    # my own methods - any name without __ is fine, just remember self in method definition
    def show_rooms(self):
        print(self.rooms)
        # if we do not need to return anything it is a good idea to return self
        return self
    def increase_room_size(self, rooms_to_add=1, verbose=False):
        self.rooms += rooms_to_add
        if verbose:
            print(f"Added {rooms_to_add} rooms to the house")
            print(f"Now we have {self.rooms} rooms")
        return self
    def print_address(self):
        if self.address:
            print(f"Address of house called {self.name} is {self.address}")
        return self
    def show_floors(self):
        print(self.floors)
        return self
    def increase_floors(self, floors_to_add=1, verbose=False):
        self.floors += floors_to_add
        if verbose:
            print(f"Added {floors_to_add} floors to the house")
            print(f"Now we have {self.floors} floors")
        return self
    


oak_street_house = []
for i in range(5):
    oak_street_house.append(ModernHouse(name=f"House No. {i+1}", address=f"Oak street {i+1}", floors=2))

print(oak_street_house[1].show_floors())

oak_street_house[2].show_rooms()
print(oak_street_house[2].name)


