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


class Llama:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
ted = Llama("Ted", "Llama", "afternoon")

class Wolf:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
joe = Wolf("Joe", "Wolf", "morning")

class Bear:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
xi = Bear("Xi", "Bear", "afternoon")

class Kangooro:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
jumpie = Kangooro("Jumpie", "Kangooro", "afternoon")

class Pig:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
frajola = Pig('Frajola', "Pig", "morning")

class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
penelope = Snake("Penelope", "Snake")

class Kobra:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
jonathan = Kobra("Jonathan", "Kobra")


class Salamander:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
piupiu = Salamander("Piupiu", "Salamander")


class Crocodile:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
jeferson = Crocodile("Jeferson", "Crocodile")

class Aligator:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
bob = Aligator("Bob", "Aligator")

class Crabby:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
krabby = Crabby("Krabby", "Crabby")

class Seahorse:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
rapidash = Seahorse("Rapidash", "Seahorse")

class Squid:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
jujuba = Squid("Jujuba", "Squid")

class Jellyfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
pikachu =   Jellyfish("Pikachu", "Jellyfish")

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True