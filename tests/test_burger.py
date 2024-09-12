from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:
    def test_burger_set_buns_true(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient_true(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_burger_remove_ingredient_true(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient]
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_burger_move_ingredient_true(self):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    def test_get_price_burger_true(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10.0
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 2.0
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 22.0

    def test_get_receipt_burger_true(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Бургерная булочка'
        mock_bun.get_price.return_value = 10.0
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'начинка'
        mock_ingredient.get_name.return_value = 'свинина'
        mock_ingredient.get_price.return_value = 2.0
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_receipt() == ('(==== Бургерная булочка ====)\n= начинка свинина =\n'
                                        '(==== Бургерная булочка ====)\n\nPrice: 22.0')
