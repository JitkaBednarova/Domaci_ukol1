import math
class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality
    
    def __str__(self):
        return f"Jméno lokality je {self.locality.name} a koeficient je {self.locality.coefficient}."

class Estate(Property):
    def __init__(self, locality, estate_typ, area):
        super().__init__(locality)
        self.estate_typ = estate_typ
        self.area = area

    def calculate_tax(self):
        if self.estate_typ == "land":
            coefficient = 0.85
        if self.estate_typ =="building site":
            coefficient = 9
        if self.estate_typ == "forrest":
            coefficient = 0.35
        return math.ceil(self.area * coefficient * self.locality.coefficient)
    
    def __str__(self):
       return super().__str__() + f"Jedná se o {self.estate_typ} má velikost {self.area}m. Daň z nemovitosti je: {self.calculate_tax()} Kč."

class Residence(Property):
    def __init__(self, locality, floor_area, commercial):
        super().__init__(locality)
        self.floor_area = floor_area
        self.commercial = commercial

    def calculate_tax(self):
        if self.commercial == "True":
            return math.ceil(self.floor_area * self.locality.coefficient * 15 * 2)
        else:
            return math.ceil(self.floor_area * self.locality.coefficient * 15)
    
    def __str__(self):
        return super().__str__() + f" Má velikost {self.floor_area} m. Jedná se o komerční objekt: {self.commercial}. Daň z nemovitosti je: {self.calculate_tax()} Kč."

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)  
land1 = Estate(manetin, "land", 900)
building1 = Residence(manetin, 120, "False")
office1 = Residence(brno, 90, "True")

print(land1)
print(building1)
print(office1)