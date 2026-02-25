from lib.recipe import Recipe

class NoSuchRecipe(Exception):
    pass


class RecipeRepository:
    def __init__(self, db_conn):
        self._conn = db_conn

    def all(self):
        rows = self._conn.execute(
            "SELECT * FROM recipes"
        )
        return [Recipe(**row) for row in rows]
    
    def find_by_name(self, name):
        formatted_name = f"%{name}%"
        rows = self._conn.execute(
            "SELECT * FROM recipes " \
            "WHERE name LIKE %s",
            [formatted_name]
        )
        if rows:
            return [Recipe(**row) for row in rows]
        else:
            raise NoSuchRecipe(f"No recipes matching {name}")