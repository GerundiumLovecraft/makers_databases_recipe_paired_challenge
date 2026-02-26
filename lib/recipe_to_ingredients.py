from lib.base_models import Model
from lib.recipe import Recipe


class ExtendedIngredientsDTO(Model):
    def __init__(self, name, spiciness, amount, unit):
        self.name = name
        self.spiciness = spiciness
        self.amount = amount
        self.unit = unit


class RecipeToIngredients(Model):
    def __init__(self, recipe_id, ingredient_id, amount, unit):
        self.recipe_id = recipe_id
        self.ingredient = ingredient_id
        self.amount = amount
        self.unit = unit


class ExtendedRecipeDTO(Model):
    def __init__(self, recipe: Recipe, ingredients: ExtendedIngredientsDTO):
        self.recipe = recipe
        self.ingredients = ingredients
