import unittest
from gen_bin_tree_l3 import gen_bin_tree


def run_tests():
    """Запуск всех тестов"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinaryTree)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


class TestBinaryTree(unittest.TestCase):

    def test_height_zero(self):
        """Тест 1: Дерево высотой 0"""
        result = gen_bin_tree(0, 12)
        self.assertIsNone(result)

    def test_height_one(self):
        """Тест 2: Дерево высотой 1"""
        result = gen_bin_tree(1, 12)
        expected = {
            'root': 12,
            'left': None,
            'right': None
        }
        self.assertEqual(result, expected)

    def test_height_two_standard_functions(self):
        """Тест 3: Дерево высотой 2"""
        result = gen_bin_tree(2, 12)
        expected = {
            'root': 12,
            'left': {
                'root': 1728,
                'left': None,
                'right': None
            },
            'right': {
                'root': 23,
                'left': None,
                'right': None
            }
        }
        self.assertEqual(result, expected)

    def test_height_three_standard_functions(self):
        """Тест 4: Дерево высотой 3"""
        result = gen_bin_tree(3, 2)
        # Проверяем структуру дерева
        self.assertEqual(result['root'], 2)
        self.assertEqual(result['left']['root'], 8)
        self.assertEqual(result['right']['root'], 3)
        self.assertEqual(result['left']['left']['root'], 512)
        self.assertEqual(result['left']['right']['root'], 15)
        self.assertEqual(result['right']['left']['root'], 27)
        self.assertEqual(result['right']['right']['root'], 5)

    def test_negative_root_value(self):
        """Тест 9: Отрицательное значение корня"""
        result = gen_bin_tree(2, -12)
        self.assertEqual(result['root'], -12)
        self.assertEqual(result['left']['root'], -1728)
        self.assertEqual(result['right']['root'], -25)

    def test_zero_root_value(self):
        """Тест 10: Нулевое значение корня"""
        result = gen_bin_tree(2, 0)
        self.assertEqual(result['root'], 0)
        self.assertEqual(result['left']['root'], 0)
        self.assertEqual(result['right']['root'], -1)


if __name__ == "__main__":
    success = run_tests()
