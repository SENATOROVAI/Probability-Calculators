# test_probability.py

import unittest
from probability import calculator_probability


class TestProbability(unittest.TestCase):
    def test_coin(self):
        # Здесь вы должны подменить функцию get_value, чтобы она возвращала "coin" и любое значение
        # Например, можно использовать mock из библиотеки unittest.mock
        from unittest.mock import patch

        with patch("app.main", return_value=("coin", "heads")):
            result = calculator_probability()
            self.assertEqual(result, "50.0%")

    def test_dice(self):
        # Здесь вы должны подменить функцию get_value, чтобы она возвращала "dice" и любое значение
        from unittest.mock import patch

        with patch("app.main", return_value=("dice", 1)):
            result = calculator_probability()
            self.assertEqual(result, "16.7%")


if __name__ == "__main__":
    unittest.main()

    # мы создаем тестовый класс TestProbability, который наследуется от unittest.TestCase.
    # Мы определяем два метода: test_coin и test_dice, которые тестируют функцию calculator_probability для разных типов событий.
# Мы используем patch из unittest.mock, чтобы подменить функцию get_value, чтобы она возвращала нужные значения для тестирования.
# Затем мы проверяем, что результат функции calculator_probability соответствует ожидаемому значению.
# Чтобы запустить тесты, выполните файл test_probability.py.
# Если все тесты пройдут успешно, то вы увидите вывод, указывающий на то, что все тесты прошли успешно.
