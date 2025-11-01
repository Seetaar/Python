class TestMySolution:
    """
    Класс для тестирования.
    """

    def __init__(self):
        """
        Инициализирует TestMySolution.
        """
        pass

    def test(self, nums, target):
        """
        Проверяет корректность входных данных.
            nums(list) - Список чисел для проверки
            target(int) - Целевое число для проверки
        Returns:
            er1 - некорректные данные
            er2 - недостаточно чисел
            True - данные корректны
        """
        if not isinstance(target, int):
            return 'er1'
        if not isinstance(nums, list):
            return 'er1'
        if not all(isinstance(x, int) for x in nums):
            return 'er1'
        if len(nums) < 2:
            return 'er2'
        return True

    def sum(self, nums, target):
        """
        Находит индексы двух чисел в списке nums, сумма которых равна target.
        """
        y = self.test(nums, target)
        if y == True:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return i, j
            return 'нет подходящих пар'
        else:
            return 'некорректные данные'


if __name__ == "__main__":
    solution = TestMySolution()

    print(solution.sum(['a', 'a', 'a'], 2))  # некорректные данные
    print(solution.sum([1, 1, 1], 2))  # (0,1)
