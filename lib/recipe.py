class Recipe:

    def __init__(self, id, name, recipe, cooking_time, rating, ingredients=None):
        self.id = id
        self.name = name
        self.recipe = recipe
        self.cooking_time = cooking_time
        self.rating = rating
        self.ingredients = ingredients if ingredients else []

    
    def __eq__(self, another_recipe):
        return self.__dict__ == another_recipe.__dict__
    
    def __repr__(self):
        return f"""
    ________________________\n
    Dish: {self.name}\n
    Recipe: {self.recipe}\n
    Cooking time: {self.cooking_time} min\n
    Rating: {self.rating} stars\n"""