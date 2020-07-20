from datetime import date

# Define custom types for the three different animal attractions at Critters and Croquettes -- PettingZoo, SnakePit, and Wetlands
# Give them each properties of attraction_name, description and animals
# attraction_name and description should be set when a habitat is instantiated, so be sure to have your __init__ method take a arguments for setting those values
# Give animals an ititial value of an empty list
# Define a method on each class for adding animals to its animals array. Note that we did not do that in the example above. so, don't just copy and paste PettingZoo
# Once you have instances of your animals and attractions created, assign your critters to their appropriate attraction.
# Output a report to the terminal that displays each attraction and its animals.

# Atractions
class PettingZoo:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animals(self, *animals):
        self.animals.extend([animals])

class SnakePit:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
    def add_animals(self, *animals):
        self.animals.extend([animals])

class Wetlands:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
    def add_animals(self, *animals):
        self.animals.extend([animals])



## Animals
class Llama:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    # def __str__(self):
    #     return f"{self.name} is a {self.species}"
ted = Llama("Ted", "Llama", "afternoon", "Llama Food")

class Wolf:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
        
joe = Wolf("Joe", "Wolf", "morning", "Wolf food")

class Bear:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
xi = Bear("Xi", "Bear", "afternoon", "bear Food")

class Kangooro:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
jumpie = Kangooro("Jumpie", "Kangooro", "afternoon", "Straw")

class Pig:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
frajola = Pig('Frajola', "Pig", "morning", "Pig Food")

class Snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
penelope = Snake("Penelope", "Snake", "Live Mouses")

class Kobra:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
jonathan = Kobra("Jonathan", "Kobra", "Live Mouses")


class Salamander:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
piupiu = Salamander("Piupiu", "Salamander", "Salamander Food")


class Crocodile:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
jeferson = Crocodile("Jeferson", "Crocodile", "Alive Sheep")

class Aligator:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
bob = Aligator("Bob", "Aligator", "Live Aligator")

class Crabby:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
krabby = Crabby("Krabby", "Crabby", "Crabby Food")

class Seahorse:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
rapidash = Seahorse("Rapidash", "Seahorse", "Seahorse Food")

class Squid:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
jujuba = Squid("Jujuba", "Squid", "squid Food")

class Jellyfish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
pikachu =   Jellyfish("Pikachu", "Jellyfish", "Jellyfish Food")

class Fish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
seaking = Fish("Seaking", "Fish", "Fish Food")

# Creating Places
village = PettingZoo("The Village", "Cozy place to todlers interact with animals")
hole = SnakePit("The Hole", "Where one can see the most dangerous snakes")
lake = Wetlands("The Lake", "Giant aquarium with lots of creatures")

village.add_animals(joe, ted, xi, jumpie, frajola)
hole.add_animals(penelope, jonathan, piupiu, jeferson, bob)
lake.add_animals(krabby, rapidash, jujuba, pikachu, seaking)

print(village.animals)
for place in [village, hole, lake]:
    print(f"{place.attraction_name}: {place.description}")
    for x in place.animals:
        for animal in x:
            print(f'You can find {animal.name} the {animal.species} in {place.attraction_name}')