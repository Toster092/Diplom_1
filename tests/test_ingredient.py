from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    def test_get_price_true(self):
        ingredient = Ingredient('начинка', 'свинина', 20.0)
        assert ingredient.get_price() == 20.0

    def test_get_name_true(self):
        ingredient = Ingredient('соус', 'сырный', 10.0)
        assert ingredient.get_name() == 'сырный'

    @pytest.mark.parametrize('ingredient_type,name,price', [('начинка', 'свинина', 10.0),('соус', 'сырный', 10.0)])
    def test_get_type_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == 'начинка' or 'соус'