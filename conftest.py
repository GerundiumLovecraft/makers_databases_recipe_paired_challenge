from pytest import fixture

from lib.database_connection import DatabaseConnection
from lib.ingredient import Ingredient
from lib.recipe import Recipe


@fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed()
    return conn


ingredients_list = [
    Ingredient(1, 'Chicken Breast', 1),
    Ingredient(2, 'Red Chili', 5),
    Ingredient(3, 'Garlic', 2),
    Ingredient(4, 'Coconut Milk', 1),
    Ingredient(5, 'Pasta', 1),
    Ingredient(6, 'Parmesan Cheese', 1),
    Ingredient(7, 'Black Pepper', 2),
    Ingredient(8, 'Cumin', 3)
]

@fixture
def recipes_list():
    return [
    Recipe(1, 'Spicy Chili Chicken', 'Sauté chicken with minced red chilis and garlic.', 30, 5),
    Recipe(2, 'Creamy Garlic Pasta', 'Boil pasta and toss with garlic and parmesan.', 20, 4),
    Recipe(3, 'Coconut Curry', 'Simmer chicken in coconut milk with cumin and spices.', 45, 5),
    Recipe(4, 'Simple Pepper Pasta', 'Toss pasta with olive oil and heavy black pepper.', 15, 3),
    Recipe(5, 'Garlic Roasted Chicken', 'Slow roast chicken with cloves of garlic.', 60, 4)
]