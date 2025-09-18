import random

# 🌟 Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# ✅ New Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# ✅ Create cats and take them for a walk
all_cats = [Bengal("Benny", 3), Chartreux("Charly", 5), Siamese("Sammy", 2)]
sara_pets = Pets(all_cats)

print("🌟 Exercise 1 Results:")
sara_pets.walk()
print("\n")


# 🌟 Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} wins the fight!"
        else:
            return f"{other_dog.name} wins the fight!"


dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 4, 25)

print("🌟 Exercise 2 Results:")
print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))
print("\n")


# 🌟 Exercise 3: PetDog
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args] + [self.name])
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")


pet_dog = PetDog("Rocky", 6, 18)
pet_dog.train()
pet_dog.play(dog1, dog2, dog3)
pet_dog.do_a_trick()
print("\n")


# 🌟 Exercise 4: Family
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family for the new child {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family {self.last_name} members:")
        for member in self.members:
            print(member)


family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

print("🌟 Exercise 4 Results:")
family.family_presentation()
print("Is Michael 18 or older?", family.is_18("Michael"))
family.born(name="Tommy", age=1, gender="Male", is_child=True)
family.family_presentation()
print("\n")


# 🌟 Exercise 5: The Incredibles
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")

    def incredible_presentation(self):
        print("✨ Here is our powerful family ✨")
        super().family_presentation()


incredibles = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

print("🌟 Exercise 5 Results:")
incredibles.incredible_presentation()
incredibles.use_power("Michael")

# Add Baby Jack
incredibles.born(name="Jack", age=1, gender="Male", is_child=True,
                 power="Unknown Power", incredible_name="BabyJack")

incredibles.incredible_presentation()
