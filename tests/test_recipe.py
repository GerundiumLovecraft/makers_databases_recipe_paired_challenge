from pytest import mark, fixture

from lib.ingredient import Ingredient
from lib.recipe import Recipe


@mark.it("Inits with expected attributes")
def test_init():
    rec = Recipe(1, "Borsch", "Boil cabbage", 45, 5)
    assert rec.id == 1
    assert rec.name == "Borsch"
    assert rec.recipe == "Boil cabbage"
    assert rec.cooking_time == 45
    assert rec.rating == 5