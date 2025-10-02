def guess_number(target: int, diap: list[int], search_type: str = 'seq') -> tuple[int, int]:
    """
    Угадывает число в списке с использованием выбранного алгоритма поиска.

    Args:
        target (int): Угадываемое число
        diap (list): Диапазон поиска
        search_type (str): Тип алгоритма поиска ('inc' - инкремент, 'bin' - бинарный поиск)

    Returns:
        tuple: (target, steps) - число и количество шагов
    """
    if search_type == 'inc':
        return inc_search(target, diap)
    elif search_type == 'bin':
        return bin_search(target, diap)
    return (target, 0)


def inc_search(target: int, diap: list[int]) -> tuple[int, int]:
    """
    Поиск числа инкрементом.

    Args:
        target (int): Угадываемое число
        diap (list): Диапазон поиска

    Returns:
        tuple: (target, steps) - число и количество шагов
    """
    steps = 0

    for num in diap:
        steps += 1
        if num == target:
            return (target, steps)

    return (target, 0)


def bin_search(target: int, diap: list[int]) -> tuple[int, int]:
    """
    Поиск числа бинарным поиском.

    Args:
        target (int): Угадываемое число
        diap (list): Диапазон поиска

    Returns:
        tuple: (target, steps) - число и количество шагов
    """
    sorted_diap = sorted(diap)
    steps = 0
    left = 0
    right = len(sorted_diap) - 1

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if sorted_diap[mid] == target:
            return (target, steps)
        elif sorted_diap[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return (target, 0)


def main():
    """
    Input угадываемого числа, диапазона и типа поиска.
    """
    try:
        target = int(input('Введите угадываемое число: '))
        start_range = int(input('Введите начало диапазона: '))
        end_range = int(input('Введите конец диапазона: '))

        if start_range > end_range:
            print("Ошибка: начало диапазона не может быть больше конца диапазона")
            return

        numbers = list(range(start_range, end_range + 1))

        print("Сортировка значений диапазона")

        search_type = input('Выберите алгоритм поиска (inc - инкремент, bin - бинарный): ')

        if search_type not in ['inc', 'bin']:
            print("Неверный тип поиска. Используется тот, который мне больше нравится.")
            search_type = 'bin'

        result, attempts = guess_number(target, numbers, search_type)

        print(f"Искомое число: {target}")
        print(f"Алгоритм поиска: {'инкремент' if search_type == 'inc' else 'бинарный'}")

        if attempts > 0:
            print(f"Потребовалось попыток: {attempts}")
        else:
            print(f"Число {target} не найдено в диапазоне")
    except ValueError:
        print("Ошибка! Вводите только целые числа")


if __name__ == '__main__':
    main()
