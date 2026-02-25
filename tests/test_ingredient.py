from pytest import mark, fixture

from lib.ingredient import Ingredient
from lib.recipe import Recipe

@mark.it("Inits with expected attributes")
def test_init():
    ing = Ingredient(1, 'Chicken Breast', 1)
    assert ing.id == 1
    assert ing.name == 'Chicken Breast'
    assert ing.spiciness == 1