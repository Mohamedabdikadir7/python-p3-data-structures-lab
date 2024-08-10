spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []  # Initialize an empty list to store the names
    for food in spicy_foods:  # Loop through each dictionary in the list
        names.append(food["name"])  # Append the value of the "name" key to the list
    return names  # Return the list of names

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  # Reuse the get_spiciest_foods function
    print_spicy_foods(spiciest_foods)  # Reuse the print_spicy_foods function

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)  # Integer division for the average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# Example usage:
print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Sichuan"))
print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))
new_food = {
    "name": "Kimchi",
    "cuisine": "Korean",
    "heat_level": 8,
}
print(create_spicy_food(spicy_foods, new_food))
