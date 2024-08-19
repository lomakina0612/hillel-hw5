
class Premises:
    def __init__(self, flooring_type, windows_count: int):
        self.flooring_type = flooring_type
        self.windows_count = windows_count

    def __str__(self):
        return f"Flooring: {self.flooring_type}, Windows: {self.windows_count}"

class RectangularPremises(Premises):
    def __init__(self, length, width, flooring_type, windows_count: int):
        super().__init__(flooring_type, windows_count)
        self.length = length
        self.width = width
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Area: {self.area} sqm, Perimeter: {self.perimeter} m, Flooring: {self.flooring_type}, Windows: {self.windows_count}"

class NonRectangularPremises(Premises):
    def __init__(self, area, perimeter, flooring_type, windows_count: int):
        super().__init__(flooring_type, windows_count)
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        return f"Area: {self.area} sqm, Perimeter: {self.perimeter} m, Flooring: {self.flooring_type}, Windows: {self.windows_count}"

class Kitchen(RectangularPremises):
    def __init__(self, length, width, flooring_type, windows_count: int, has_dishwasher, appliance_count: int):
        super().__init__(length, width, flooring_type, windows_count)
        self.has_dishwasher = has_dishwasher
        self.appliance_count = appliance_count

    def __str__(self):
        return (f"Kitchen - {super().__str__()}, Dishwasher: {'Yes' if self.has_dishwasher else 'No'}, "
                f"Appliances: {self.appliance_count}")

class Bathroom(RectangularPremises):
    def __init__(self, length, width, flooring_type, windows_count: int, has_bathtub, has_shower, has_toilet, bathroom_type):
        super().__init__(length, width, flooring_type, windows_count)
        self.has_bathtub = has_bathtub
        self.has_shower = has_shower
        self.has_toilet = has_toilet
        self.bathroom_type = bathroom_type

    def __str__(self):
        return (f"{self.bathroom_type} - {super().__str__()}, Bathtub: {'Yes' if self.has_bathtub else 'No'}, "
                f"Shower: {'Yes' if self.has_shower else 'No'}, Toilet: {'Yes' if self.has_toilet else 'No'}")

class Room(RectangularPremises):
    def __init__(self, length, width, flooring_type, windows_count: int, room_type):
        super().__init__(length, width, flooring_type, windows_count)
        self.room_type = room_type

    def __str__(self):
        return f"{self.room_type} - {super().__str__()}"

class NonRectangularRoom(NonRectangularPremises):
    def __init__(self, area, perimeter, flooring_type, windows_count: int, room_type):
        super().__init__(area, perimeter, flooring_type, windows_count)
        self.room_type = room_type

    def __str__(self):
        return f"{self.room_type} - {super().__str__()}"
    
class Flat:
    def __init__(self, address, premises):
        self.address = address
        self.premises = premises

    def total_area(self):
        return sum([premise.area for premise in self.premises])

    def __str__(self):
        return (f"Flat at {self.address}\nTotal Area: {self.total_area()} sqm\n\n" +
                "\n".join(str(premise) for premise in self.premises))

# Example
kitchen = Kitchen(3, 5, "Tile", 1, True, 4)
master_bathroom  = Bathroom(2, 4, "Marble", 1, True, True, True, "Master Bathroom")
guest_toilet = Bathroom(1.5, 2, "Tile", 0, False, False, True, "Guest Toilet")
living_room = Room(5, 4, "Wood", 1, "Living Room")
bedroom = Room(5, 3, "Carpet", 1, "Bedroom")
children_room = NonRectangularRoom(16, 18, "Wood", 2, "Children Room")
hall = NonRectangularRoom(6, 12, "Tile", 0, "Hall")
flat = Flat("22 Kanatna Street, Odesa", [kitchen, master_bathroom, guest_toilet, living_room, bedroom, children_room, hall])

print(flat)