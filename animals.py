from datetime import date

# the petting area, such as donkeys, llamas, and goats
# the glass tank, like copperheads and rat snakes
# the pond, like mallards and goldfish

# self.critters = "Petting area"
# self.critters = "Petting area"
# self.critters = "Petting area"

# self.swimming = True
# self.slithering = True
# self.walking = True
# self.food = food

class Llama:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
ted = Llama("Ted", "Llama", "afternoon", "Llama Food")

class Wolf:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
joe = Wolf("Joe", "Wolf", "morning", "Wolf food")

class Bear:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
xi = Bear("Xi", "Bear", "afternoon", "bear Food")

class Kangooro:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
jumpie = Kangooro("Jumpie", "Kangooro", "afternoon", "Straw")

class Pig:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
frajola = Pig('Frajola', "Pig", "morning", "Pig Food")

class Snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
penelope = Snake("Penelope", "Snake", "Live Mouses")

class Kobra:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
jonathan = Kobra("Jonathan", "Kobra", "Live Mouses")


class Salamander:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
piupiu = Salamander("Piupiu", "Salamander", "Salamander Food")


class Crocodile:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
jeferson = Crocodile("Jeferson", "Crocodile", "Alive Sheep")

class Aligator:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
bob = Aligator("Bob", "Aligator", "Live Aligator")

class Crabby:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
krabby = Crabby("Krabby", "Crabby", "Crabby Food")

class Seahorse:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
rapidash = Seahorse("Rapidash", "Seahorse", "Seahorse Food")

class Squid:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
jujuba = Squid("Jujuba", "Squid", "squid Food")

class Jellyfish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
pikachu =   Jellyfish("Pikachu", "Jellyfish", "Jellyfish Food")

class Fish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
seaking = Fish("Seaking", "Fish", "Fish Food")