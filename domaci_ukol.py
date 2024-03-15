import math

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(self, locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == "land":
            coefficient = 0.85
        if self.estate_type == "building site":
            coefficient = 9
        if self.estate_type == "forrest":
            coefficient = 0.35
        return  math.ceil(self.area * coefficient * self.locality.coefficient)
 
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(self, locality)
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        if self.commercial == True:
            return math.ceil(self.area * self.locality.coefficient * 15 * 2)
        else:
            return math.ceil(self.area * self.locality.coefficient * 15)
        

land1 = Estate("Manětín", "land", 900)

print(land1.calculate_tax())