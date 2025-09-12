# Exercise 1 : Hello World
print(("Hello world\n" * 4))

# Exercise 2 : Some Math
result = (99 ** 3) * 8
print(f"(99³) × 8 = {result}")

# Exercise 3 : What’s your name ?
MY_NAME = "SALAHEDDINE"  # Change this to your real name
user_name = input("What is your name? ")
if user_name.lower() == MY_NAME.lower():
    print("We have the same name ")
else:
    print(f"Nice to meet you, {user_name}! But my name is better ")

# Exercise 4 : Tall enough to ride a roller coaster
    height = int(input("ch7al tool dyalk b cm : "))
    if height > 145:
        print("✅ rak twil tbarklah bach tridi")
    else:
        print("❌ la la , mazal 9ssir")


# Exercise 5 : Favorite Numbers
my_fav_numbers = {7, 13, 21}
my_fav_numbers.update([99, 100]) # 7itach update except list set or tuple 
my_fav_numbers.remove(100)  
friend_fav_numbers = {5, 13, 42}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(f"My favorite numbers: {my_fav_numbers}")
print(f"Friend's favorite numbers: {friend_fav_numbers}")
print(f"Our favorite numbers: {our_fav_numbers}")

# Exercise 6: Tuple
my_tuple = (1, 2, 3)
print("Tuples are immutable so mn9adroch nbdlohom b7al lists. let's try ")
try:
    my_tuple.append(4)   
except AttributeError as e:
    print("❌ Mat9darch:", e)

# Exercise 7 : List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(f"Number of apples: {basket.count('Apples')}")
basket.clear()
print(f"Final basket (should be empty): {basket}")

# Exercise 8 : Sandwich Orders
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f" I made your {sandwich.lower()}")

