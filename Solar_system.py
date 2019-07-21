class System:
    
    def __init__(self):
        self.bodies = []
        
    def add(self, celestial_body):
        self.bodies.append(celestial_body)

    def total_mass(self):
        total_system_mass = 0
        for body in self.bodies:
            total_system_mass += body.mass
        return total_system_mass
        
        # total_system_mass = sum(self.bodies)
        # return total_system_mass

class Body(System):

    def __init__(self, name, mass): 
        self.name = name
        self.mass = mass

class Planet(Body):

    def __init__(self, name, mass, days, years):
        super().__init__(name, mass)
        self.days = days
        self.years = years

class Star(Body):

    def __init__(self, name, mass, star_type):
        super().__init__(name, mass)
        self.star_type = star_type

class Moon(Body):

    def __init__(self, name, mass, months, planet_orbit):
        super().__init__(name, mass)
        self.months = months
        self.planet_orbit = planet_orbit




solar_systemx = System()       
jup = Planet('Jupiter', 10000, 100, 3)
mars = Planet('Mars', 13000, 200, 6)
moonx = Moon('Moon X', 5000, 25, 'x')

solar_systemx.add(jup)
solar_systemx.add(mars)
solar_systemx.add(moonx)
# testing the TOTAL MASS METHOD
print(solar_systemx.total_mass())
print(solar_systemx.bodies)







# xyz.add(4765)
# xyz.add(88)
# xyz.add(9987)
# print(xyz.total_mass())
# jup.mass
# print(jup.mass)
# print(System)

# Inputing a systems and bodies 
# solar1 = System()
