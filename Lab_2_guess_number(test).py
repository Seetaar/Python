import unittest
from guess_number_l2 import guess_number, inc_search, bin_search


def run_tests():
    """Запуск всех тестов"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGuessNumber)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


class TestGuessNumber(unittest.TestCase):

    def test_inc_found(self):
        """Тест 1 инкремента когда число есть"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = inc_search(3, numbers)
        self.assertEqual(result, 3)
        self.assertEqual(steps, 3)

    def test_inc_not_found(self):
        """Тест 2 инкремента когда числа нет"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = inc_search(10, numbers)
        self.assertEqual(result, 10)
        self.assertEqual(steps, 0)

    def test_inc_target_start(self):
        """Тест 3 инкремента когда target = start_range"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = inc_search(1, numbers)
        self.assertEqual(result, 1)
        self.assertEqual(steps, 1)

    def test_inc_target_end(self):
        """Тест 4 инкремента когда target = end_range"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = inc_search(5, numbers)
        self.assertEqual(result, 5)
        self.assertEqual(steps, 5)

    def test_bin_found(self):
        """Тест 5 бинарного поиска когда число есть"""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result, steps = bin_search(7, numbers)
        self.assertEqual(result, 7)
        self.assertTrue(steps > 0)

    def test_bin_not_found(self):
        """Тест 6 бинарного поиска когда числа нет"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = bin_search(10, numbers)
        self.assertEqual(result, 10)
        self.assertEqual(steps, 0)

    def test_bin_target_start(self):
        """Тест 7 бинарного поиска когда target = start_range"""
        numbers = [1, 2, 3, 4, 5, 6, 7]
        result, steps = bin_search(1, numbers)
        self.assertEqual(result, 1)
        self.assertEqual(steps, 3)

    def test_bin_target_end(self):
        """Тест 8 бинарного поиска когда target = end_range"""
        numbers = [1, 2, 3, 4, 5, 6, 7]
        result, steps = bin_search(7, numbers)
        self.assertEqual(result, 7)
        self.assertEqual(steps, 3)

    def test_guess_number_inc(self):
        """Тест 9 функции guess_number с инкрементом"""
        numbers = [1, 2, 3, 4, 5]
        result, steps = guess_number(3, numbers, 'inc')
        self.assertEqual(result, 3)
        self.assertEqual(steps, 3)

    def test_inc_not_sorted(self):
        """Тест 10 бинарного поиска когда несортированный диапазон"""
        numbers = [11, 30, 44, 16, 9]
        result, steps = inc_search(44, numbers)
        self.assertEqual(result, 44)
        self.assertEqual(steps, 3)

    def test_guess_number_bin(self):
        """Тест 11 функции guess_number с бинарным поиском"""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result, steps = guess_number(7, numbers, 'bin')
        self.assertEqual(result, 7)
        self.assertTrue(steps > 0)

    def test_bin_not_sorted(self):
        """Тест 12 инкремента когда несортированный диапазон"""
        numbers = [11, 30, 44, 16, 9]
        result, steps = bin_search(16, numbers)
        self.assertEqual(result, 16)
        self.assertEqual(steps, 1)


if __name__ == "__main__":
    success = run_tests()
