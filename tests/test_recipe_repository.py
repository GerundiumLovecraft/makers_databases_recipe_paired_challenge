from pytest import mark, fixture

from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

@fixture
def rec_repo(db_connection):
    return RecipeRepository(db_connection)


@mark.it("all() returns list of Recipe objects")
def test_all(rec_repo):
    output = rec_repo.all()
    assert all(isinstance(x, Recipe) for x in output)


@mark.it("all() returns Recipe object for every record in recipes table")
def test_all_recs(rec_repo, recipes_list):
    output = rec_repo.all()
    assert output == recipes_list


@mark.it("find_by_name() returns Recipe object matching passed name")
def test_by_name(rec_repo, recipes_list):
    output = rec_repo.find_by_name("Curry")
    assert output == [recipes_list[2]]


@mark.it("find_by_spiciness() returns Recipe objects matching passed spiciness")
def test_by_spice(rec_repo, recipes_list):
    output = rec_repo.find_by_spiciness(5)
    assert output == [recipes_list[0]]



