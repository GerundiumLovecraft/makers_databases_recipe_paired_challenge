from lib.base_models import Repository
from lib.recipe_to_ingredients import RecipeToIngredients, ExtendedRecipeDTO, ExtendedIngredientsDTO
from lib.recipe import Recipe


class RecipeToIngredientsRepository(Repository):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self._get_current_ingredients()
    
    def add_recipe(self, recipe: Recipe):
        rows = self._connection.execute(
            "INSERT INTO recipes "
            "  (name, recipe, cooking_time, rating) "
            "VALUES "
            " (%s, %s, %s, %s) "
            "RETURNING id",
            [recipe.name, recipe.recipe, recipe.cooking_time, recipe.rating]
        )

        rec_id = rows[0]['id']

        missing_ings = self._check_for_missing_ingredients(recipe.ingredients)

        self._add_missing_ingredients(missing_ings)


    def _add_recipe_to_ingredient(self, r_to_i: RecipeToIngredients):
        pass


    def _add_missing_ingredients(self, ingredients: list[ExtendedIngredientsDTO]):
        query = "INSERT INTO ingredients (name, spiciness) VALUES " 


        placeholders = []
        query_params = []

        for ing in ingredients:
            placeholders.append("(%s, %s)")
            query_params.extend([ing.name, ing.spiciness])
        
        placeholder_str = ", ".join(placeholders)
        query += placeholder_str
        query += " RETURNING id"

        rows = self._connection.execute(query, query_params)
    

    def _check_for_missing_ingredients(self, list_of_ings: list[ExtendedIngredientsDTO]):
        ing_names = set([i['name'] for i in list_of_ings])
        return ing_names.difference(self._current_ingredients)

    def _get_current_ingredients(self):
        rows = self._connection.execute("SELECT name FROM ingredients")
        setattr(self, "_current_ingredients", set([row['name'] for row in rows]))
        
        