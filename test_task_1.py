from unittest import TestCase
from parameterized import parameterized

import task_1


class Test(TestCase):

    @parameterized.expand([
        [0.5, 0.9011822485427146],
        [1.0, 2.1959666505084225],
        [-1.0, 0.47572822655522023]
    ])
    def test_expr_1(self, x: float, exp: float):
        # Вычисление
        act = task_1.expr_1(x)
        # Проверка
        self.assertEqual(exp, act, "Не работает вычисление")


    @parameterized.expand([
        [0.5, -0.6933077156249191],
        [1.0, 0.38832597549414927]
    ])
    def test_expr_3(self, x: float, exp: float):
        # Вычисление
        act = task_1.expr_3(x)
        # Проверка
        self.assertEqual(exp, act, "Не работает вычисление")
