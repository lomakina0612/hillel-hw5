
class Premises:
    def __init__(self, shape="rectangle", flooring_type="Tile", windows_count=1, 
                 length=None, width=None, area=None, perimeter=None):
# give length and width for a rectangle shape
        self.flooring_type = flooring_type
        self.windows_count = windows_count
        self.shape = shape

        if self.shape == "rectangle" and length is not None and width is not None:
            self.length = length
            self.width = width
            self.area = self.calculate_area()
            self.perimeter = self.calculate_perimeter()
        elif self.shape == "complex" and area is not None and perimeter is not None:
            self.area = area
            self.perimeter = perimeter
        else:
            raise ValueError("Invalid parameters for the given shape")

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return (f"Shape: {self.shape}, Area: {self.area} sqm, Perimeter: {self.perimeter} m, "
                f"Flooring: {self.flooring_type}, Windows: {self.windows_count}")

class Kitchen(Premises):
    def __init__(self, shape="rectangle", flooring_type="Tile", windows_count=1, length=None, 
                 width=None, area=None, perimeter=None, appliance_count=1, has_dishwasher=True):
        super().__init__(shape=shape, flooring_type=flooring_type, windows_count=windows_count, 
                         length=length, width=width, area=area, perimeter=perimeter)
        self.has_dishwasher = has_dishwasher
        self.appliance_count = appliance_count

    def __str__(self):
        return (f"Kitchen - {super().__str__()}, Appliances: {self.appliance_count}, "
                f"Dishwasher: {'Yes' if self.has_dishwasher else 'No'}")

class Bathroom(Premises):
    def __init__(self, shape="rectangle", flooring_type="Tile", windows_count=0, length=None, 
                 width=None, area=None, perimeter=None, room_type="Bathroom", has_bathtub=False, has_shower=True, has_toilet=True):
        super().__init__(shape=shape, flooring_type=flooring_type, windows_count=windows_count, 
                         length=length, width=width, area=area, perimeter=perimeter)
        
        self.has_bathtub = has_bathtub
        self.has_shower = has_shower
        self.has_toilet = has_toilet
        self.room_type = room_type

    def __str__(self):
        return (f"{self.room_type} - {super().__str__()}, Bathtub: {'Yes' if self.has_bathtub else 'No'}, "
                f"Shower: {'Yes' if self.has_shower else 'No'}, Toilet: {'Yes' if self.has_toilet else 'No'}")

class Room(Premises):
    def __init__(self, room_type="Room", shape="rectangle", flooring_type="Wood", windows_count=1, 
                 length=None, width=None, area=None, perimeter=None):
        super().__init__(shape=shape, flooring_type=flooring_type, windows_count=windows_count, 
                         length=length, width=width, area=area, perimeter=perimeter)

        self.room_type = room_type

    def __str__(self):
        return f"{self.room_type} - {super().__str__()}"
    
class Flat:
    def __init__(self, address, premises = None):
        self.address = address
        self.premises = premises if premises else []
    
    def add_premise(self, premise):
        self.premises.append(premise)

    def remove_premise(self, premise):
        self.premises.remove(premise)

    def total_area(self):
        return sum([premise.area for premise in self.premises])

    def __str__(self):
        return (f"Flat at {self.address}\nTotal Area: {self.total_area()} sqm\n\n" +
                "\n".join(str(premise) for premise in self.premises))

# Example

kitchen = Kitchen(length=5, width=3, appliance_count=4)
master_bathroom  = Bathroom(room_type="Master Bathroom", length=4, width=2, flooring_type="Marble", windows_count=1, has_bathtub=True)
guest_toilet = Bathroom(room_type="Guest Toilet", length=2, width=1.5, has_shower=False)
living_room = Room(room_type="Living Room", length=5, width=4)
bedroom = Room(room_type="Bedroom", length=5, width=3,  flooring_type="Carpet")
children_room = Room(room_type="Children Room", shape="complex", windows_count=2, area=16, perimeter=18)
hall = Room(room_type="Hall", shape="complex", windows_count=0, area=6, perimeter=12, flooring_type="Tile")


flat = Flat("22 Kanatna Street, Odesa")
flat.add_premise(kitchen)
flat.add_premise(master_bathroom)
flat.add_premise(guest_toilet)
flat.add_premise(living_room)
flat.add_premise(bedroom)
flat.add_premise(children_room)
flat.add_premise(hall)

print(flat)