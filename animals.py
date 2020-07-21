from datetime import date

### Atractions
class PettingZoo:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animals(self, *animals):
        self.animals.extend(list(animals))

class SnakePit:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
    def add_animals(self, *animals):
        self.animals.extend(list(animals))

    @property
    def last_critter_added(self):
        print(f"{self.animals[-1].name} the {self.animals[-1].species}")

class Wetlands:
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
    def add_animals(self, *animals):
        self.animals.extend(list(animals))



### Animals

class Animal:

    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_num = chip_num

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

ted = Llama("Ted", "Llama", "afternoon", "Llama Food", 1)
print(ted)
ted.feed()

class Wolf(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
        
joe = Wolf("Joe", "Wolf", "morning", "Wolf food", 2)

class Bear(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
xi = Bear("Xi", "Bear", "afternoon", "Bear Food", 3)

class Kangooro(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
jumpie = Kangooro("Jumpie", "Kangooro", "afternoon", "Straw", 4)

class Pig(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
frajola = Pig('Frajola', "Pig", "morning", "Pig Food", 5)

class Snake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

penelope = Snake("Penelope", "Snake", "Live Mouses", 6)

class Kobra(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
jonathan = Kobra("Jonathan", "Kobra", "Live Mouses", 7)


class Salamander(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
piupiu = Salamander("Piupiu", "Salamander", "Salamander Food", 8)


class Crocodile(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
jeferson = Crocodile("Jeferson", "Crocodile", "Alive Sheep", 9)

class Aligator(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
bob = Aligator("Bob", "Aligator", "Live Aligator", 10)

class Crabby(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

krabby = Crabby("Krabby", "Crabby", "Crabby Food", 11)

class Seahorse(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
rapidash = Seahorse("Rapidash", "Seahorse", "Seahorse Food", 12)

class Squid(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
jujuba = Squid("Jujuba", "Squid", "squid Food", 13)

class Jellyfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
pikachu =   Jellyfish("Pikachu", "Jellyfish", "Jellyfish Food", 14)

class Fish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
seaking = Fish("Seaking", "Fish", "Fish Food", 15)

# Creating Places
village = PettingZoo("The Village", "Cozy place to todlers interact with animals")
hole = SnakePit("The Hole", "Where one can see the most dangerous snakes")
lake = Wetlands("The Lake", "Giant aquarium with lots of creatures")

village.add_animals(joe, ted, xi, jumpie, frajola)
hole.add_animals(penelope, jonathan, piupiu, jeferson, bob)
lake.add_animals(krabby, rapidash, jujuba, pikachu, seaking)

