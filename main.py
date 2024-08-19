class Premises:
    def __init__(self, flooring_type):
        self.flooring_type = flooring_type

    def __str__(self):
        return f"Flooring: {self.flooring_type}"

class RectangularPremises(Premises):
    def __init__(self, length, width, flooring_type):
        self.length = length
        self.width = width
        self.flooring_type = flooring_type
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Area: {self.area} sqm, Perimeter: {self.perimeter} m, Flooring: {self.flooring_type}"

class NonRectangularPremises(Premises):
    def __init__(self, area, perimeter, flooring_type):
        super().__init__(flooring_type)
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        return f"Area: {self.area} sqm, Perimeter: {self.perimeter} m, Flooring: {self.flooring_type}"

class Kitchen(RectangularPremises):
    def __init__(self, length, width, flooring_type, has_dishwasher, appliance_count):
        super().__init__(length, width, flooring_type)
        self.has_dishwasher = has_dishwasher
        self.appliance_count = appliance_count

    def __str__(self):
        return (f"Kitchen - {super().__str__()}, Dishwasher: {'Yes' if self.has_dishwasher else 'No'}, "
                f"Appliances: {self.appliance_count}")

class Bathroom(RectangularPremises):
    def __init__(self, length, width, flooring_type, has_bathtub, has_shower):
        super().__init__(length, width, flooring_type)
        self.has_bathtub = has_bathtub
        self.has_shower = has_shower

    def __str__(self):
        return (f"Bathroom - {super().__str__()}, Bathtub: {'Yes' if self.has_bathtub else 'No'}, "
                f"Shower: {'Yes' if self.has_shower else 'No'}")

class Room(RectangularPremises):
    def __init__(self, length, width, flooring_type, room_type):
        super().__init__(length, width, flooring_type)
        self.room_type = room_type

    def __str__(self):
        return f"{self.room_type} - {super().__str__()}"

class NonRectangularRoom(NonRectangularPremises):
    def __init__(self, area, perimeter, flooring_type, room_type):
        super().__init__(area, perimeter, flooring_type)
        self.room_type = room_type

    def __str__(self):
            return f"{self.room_type} - {super().__str__()}"
    
class Flat:
    def __init__(self, address, rooms:list, kitchen, bathroom):
        self.address = address
        self.rooms = rooms  # List of Room objects
        self.kitchen = kitchen
        self.bathroom = bathroom

    def total_area(self):
        return sum([room.area for room in self.rooms]) + self.kitchen.area + self.bathroom.area

    def __str__(self):
        return (f"Flat at {self.address}\nTotal Area: {self.total_area()} sqm\n\n"
                f"{self.kitchen}\n{self.bathroom}\n" +
                "\n".join(str(room) for room in self.rooms))


# Приклад використання



kitchen = Kitchen(3, 5, "Tile", True, 4)
bathroom = Bathroom(2, 4, "Marble", True, True)
living_room = Room(5, 4, "Wood", "Living Room")
bedroom = Room(5, 3, "Carpet", "Bedroom")
children_room = NonRectangularRoom(16, 18, "Wood", "Children room")
terrace = NonRectangularRoom(6, 12, "Tile", "Terrace")
flat = Flat("22 Kanatna Street, Odesa", [living_room, bedroom, children_room, terrace], kitchen, bathroom)

print(flat)