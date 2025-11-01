import unittest
from TwoSumMain import TestMySolution


class TestMySolution(unittest.TestCase):
    def setUp(self):
        self.solution = TestMySolution()

    def test_find_pair_success(self):
        """
        Тест успешного нахождения пары чисел.
        """
        result = self.solution.sum([3, 3, 3, 3], 6)
        self.assertEqual(result, (0, 1))

    def test_no_suitable_pair(self):
        """
        Тест отсутствия подходящей пары чисел.
        """
        result = self.solution.sum([3, 3, 3, 3], 7)
        self.assertEqual(result, 'нет подходящих пар')

    def test_empty_list(self):
        """
        Тест пустого списка nums.
        """
        result = self.solution.sum([], 8)
        self.assertEqual(result, 'недостаточно чисел')

    def test_single_element_list(self):
        """
        Тест списка nums с недостаточным кол-вом чисел.
        """
        result = self.solution.sum([3], 6)
        self.assertEqual(result, 'недостаточно чисел')

    def test_single_element_equals_target(self):
        """
        Тест списка nums с одним элементом, равным target.
        """
        result = self.solution.sum([3], 3)
        self.assertEqual(result, 'недостаточно чисел')

    def test_zero_target_no_zero_pair(self):
        """
        Тест target = 0.
        """
        result = self.solution.sum([12, 53, 543, 0], 0)
        self.assertEqual(result, 'нет подходящих пар')

    def test_string_instead_of_list(self):
        """
        Тест str в списке nums.
        """
        result = self.solution.sum('nums', 6)
        self.assertEqual(result, 'некорректные данные')

    def test_float_numbers_in_list(self):
        """
        Тест float в списке nums.
        """
        result = self.solution.sum([3.5, 12.78], 6)
        self.assertEqual(result, 'некорректные данные')

    def test_string_instead_of_target(self):
        """
        Тест str в target.
        """
        result = self.solution.sum([3, 3, 3, 3], 'target')
        self.assertEqual(result, 'некорректные данные')


if __name__ == '__main__':
    unittest.main()
