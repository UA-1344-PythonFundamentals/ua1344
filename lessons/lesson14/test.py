import unittest

from .funk import solve_quadratic_equation


class TestQuadraticEquationSolver(unittest.TestCase):

    def test_two_distinct_roots(self):
        # Тестуємо випадок з двома різними дійсними коренями
        a = 1
        b = -3
        c = 2
        expected_roots = (2.0, 1.0)  # Порядок не важливий
        actual_roots = solve_quadratic_equation(a, b, c)
        self.assertIsNotNone(actual_roots)
        self.assertAlmostEqual(actual_roots[0], expected_roots[0])
        self.assertAlmostEqual(actual_roots[1], expected_roots[1])

    # def test_one_real_root(self):
    #     # Тестуємо випадок з одним дійсним коренем (або двома рівними)
    #     a = 1
    #     b = -2
    #     c = 1
    #     expected_roots = (1.0, 1.0)
    #     actual_roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNotNone(actual_roots)
    #     self.assertAlmostEqual(actual_roots[0], expected_roots[0])
    #     self.assertAlmostEqual(actual_roots[1], expected_roots[1])

    def test_no_real_roots(self):
        # Тестуємо випадок, коли немає дійсних коренів
        a = 1
        b = 1
        c = 1
        actual_roots = solve_quadratic_equation(a, b, c)
        self.assertIsNone(actual_roots)

    # def test_a_is_zero(self):
    #     # Перевірка, коли a = 0 (не квадратне рівняння)
    #     a = 0
    #     b = 2
    #     c = 3
    #     # Очікуємо, що функція поверне розв'язок лінійного рівняння, або може викликати помилку.
    #     # В даному випадку, повертаємо (-c/b, -c/b), але це можна змінити, якщо потрібно інша поведінка.
    #     expected_roots = (-1.5, -1.5)
    #     actual_roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNotNone(actual_roots)
    #     self.assertAlmostEqual(actual_roots[0], expected_roots[0])
    #     self.assertAlmostEqual(actual_roots[1], expected_roots[1])

    # def test_large_coefficients(self):
    #     # Тестуємо з великими коефіцієнтами
    #     a = 1000
    #     b = -2000
    #     c = 1000
    #     expected_roots = (1.0, 1.0)
    #     actual_roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNotNone(actual_roots)
    #     self.assertAlmostEqual(actual_roots[0], expected_roots[0])
    #     self.assertAlmostEqual(actual_roots[1], expected_roots[1])


if __name__ == "__main__":
    unittest.main()
