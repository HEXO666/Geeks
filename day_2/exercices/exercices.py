# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for member, age in family.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
    print(f"{member} has to pay: ${cost}")
print(f"Total cost: ${total_cost}")

# Exercise 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print("Zara clients are", brand["type_of_clothes"])
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print("Last competitor:", brand["international_competitors"][-1])
print("US colors:", brand["major_color"]["US"])
print("Number of pairs:", len(brand))
print("Keys:", brand.keys())
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print("Updated number_stores:", brand["number_stores"])

# Exercise 4
def describe_city(city, country="Morocco"):
    print(f"{city} is in {country}")

describe_city("Casablanca")
describe_city("Reykjavik", "Iceland")

# Exercise 5
import random
def compare_numbers(num):
    rand_num = random.randint(1, 100)
    if num == rand_num:
        print("Success! Both numbers are the same.")
    else:
        print(f"Fail! Your number: {num}, Random number: {rand_num}")

compare_numbers(25)

# Exercise 6
def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'")

make_shirt()
make_shirt("Medium")
make_shirt("Small", "Custom Message")
make_shirt(size="XL", message="Keyword Arg Example")

# Exercise 7
def get_random_temp(season="summer"):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(0, 23)
    elif season == "summer":
        return random.uniform(16, 40)
    elif season == "autumn":
        return random.uniform(0, 23)
    return random.uniform(-10, 40)

def main():
    season = input("Enter a season (winter, spring, summer, autumn): ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f}°C")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("Nice weather.")
    elif temp < 32:
        print("Warm and pleasant.")
    else:
        print("It’s really hot! Stay hydrated.")

# main()  # Uncomment to run interactively

# Exercise 8
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def star_wars_quiz():
    correct = 0
    wrong_answers = []
    for q in data:
        user_ans = input(q["question"] + " ")
        if user_ans.strip().lower() == q["answer"].lower():
            correct += 1
        else:
            wrong_answers.append((q["question"], user_ans, q["answer"]))
    print(f"Correct: {correct}, Incorrect: {len(data) - correct}")
    if wrong_answers:
        print("\nReview of wrong answers:")
        for q, ua, ca in wrong_answers:
            print(f"Q: {q}\nYour answer: {ua}\nCorrect: {ca}\n")
    if len(wrong_answers) > 3:
        print("You had more than 3 wrong answers. Try again!")

# star_wars_quiz()  # Uncomment to play

