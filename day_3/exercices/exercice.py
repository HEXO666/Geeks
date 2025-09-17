# 🌟 Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Function to find the oldest cat
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

# Instantiate cats
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Shadow", 3)

cats = [cat1, cat2, cat3]
oldest_cat = find_oldest_cat(cats)

print("\n🌟 Exercise 1: Cats")
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# 🌟 Exercise 2: Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# David’s dog
davids_dog = Dog("Rex", 50)
print("\n🌟 Exercise 2: Dogs")
print(f"David's dog: {davids_dog.name}, {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

# Sarah’s dog
sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog: {sarahs_dog.name}, {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Which dog is bigger?
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")


# 🌟 Exercise 3: Song
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

print("\n🌟 Exercise 3: Song")
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()


# 🌟 Exercise 4: Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            key = animal[0].upper()
            if key not in sorted_animals:
                sorted_animals[key] = []
            sorted_animals[key].append(animal)
        return sorted_animals

    def get_groups(self):
        groups = self.sort_animals()
        for key, group in groups.items():
            print(f"{key}: {group}")

print("\n🌟 Exercise 4: Zoo")
new_york_zoo = Zoo("New York Zoo")

# Add animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Eel")

# Display animals
new_york_zoo.get_animals()

# Sell an animal
new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()

# Group animals
print("Animal groups:")
new_york_zoo.get_groups()
