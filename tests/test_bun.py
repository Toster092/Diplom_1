from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name_true(self):
        bun = Bun('Бургерная булочка', 10.0)
        assert bun.get_name() == 'Бургерная булочка'

    def test_bun_get_price_true(self):
        bun = Bun('Бургерная булочка', 10.0)
        assert bun.get_price() == 10.0