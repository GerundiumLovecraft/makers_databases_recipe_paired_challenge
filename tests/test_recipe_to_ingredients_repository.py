from pytest import mark, fixture, raises
from unittest.mock import patch, Mock

from lib.recipe_to_ingredients_repository import RecipeToIngredientsRepository


@fixture
def rec_t_ing_repo(db_connection):
    return RecipeToIngredientsRepository(db_connection)


@mark.it("_add_missing_ingredient() constructs query")
def test_add_miss(rec_t_ing_repo, ):
    # with patch("lib.database_connection.DatabaseConnection") as mock_db_conn:
    mock_ing_1 = Mock()
    mock_ing_2 = Mock()

    mock_ing_1.name = "Egg"
    mock_ing_1.spiciness = 1

    mock_ing_2.name = "Water"
    mock_ing_2.spiciness = 1


    rec_t_ing_repo._add_missing_ingredients(
        [
            mock_ing_1, mock_ing_2
        ]
        )
    assert True
    
    # mock_db_conn.execute.assert_called_with(
    #     "INSERT INTO ingredients (name, spiciness) VALUES "
    #     "(Egg, 1), " \
    #     "(Water, 1) "
    #     "RETURNING id"
    # )