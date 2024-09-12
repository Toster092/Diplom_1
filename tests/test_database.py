from praktikum.database import Database
from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
    ])
    def test_available_buns_true(self, name, price):
        database = Database()
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        database.buns = [mock_bun]
        database.available_buns()
        assert database.available_buns() == [mock_bun]

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE,'hot sauce', 100),
        (INGREDIENT_TYPE_SAUCE,'sour cream', 200),
        (INGREDIENT_TYPE_SAUCE,'chili sauce', 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_available_ingredients_true(self, ingredient_type, name, price):
        database = Database()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        database.ingredients = [mock_ingredient]
        assert database.available_ingredients() == [mock_ingredient]
