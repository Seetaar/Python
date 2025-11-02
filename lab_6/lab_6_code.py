import timeit
import matplotlib.pyplot as plt
import random
from functools import lru_cache
from collections import deque


def gen_bin_tree_recursive(height=12, root=4, l_b=lambda x: x**3, r_b=lambda y: y*2-1):
    """
    Генерирует бинарное дерево рекурсивным способом.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: лямбда-функция для вычисления левой ветви
        r_b: лямбда-функция для вычисления правой ветви

    Returns:
        Бинарное дерево в виде словаря, или None если высота меньше или равна 0
    """
    if height <= 0:
        return None

    left_tree = gen_bin_tree_recursive(height - 1, l_b(root))
    right_tree = gen_bin_tree_recursive(height - 1, r_b(root))

    return {
        'value': root,
        'left': left_tree,
        'right': right_tree
    }


def gen_bin_tree_iterative(height=4, root=3, l_b=lambda x: x + 2, r_b=lambda y: y * 3):
    """
    Генерирует бинарное дерево итеративно.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: лямбда-функция для вычисления левой ветви
        r_b: лямбда-функция для вычисления правой ветви

    Returns:
        Словарь (dict), или None если высота меньше или равна 0
    """

    if height <= 0:
        return None

    bin_tree = {'value': root, 'left': None, 'right': None}

    line = deque()
    line.append((bin_tree, 1))

    while line:
        current_node, current_level = line.popleft()
        if current_level < height:
            # Левая ветвь
            left_value = l_b(current_node['value'])
            left_node = {'value': left_value, 'left': None, 'right': None}
            current_node['left'] = left_node
            line.append((left_node, current_level + 1))

            # Правая ветвь
            right_value = r_b(current_node['value'])
            right_node = {'value': right_value, 'left': None, 'right': None}
            current_node['right'] = right_node
            line.append((right_node, current_level + 1))

    return bin_tree


@lru_cache
def gen_bin_tree_recursive_cache(height=4, root=3, l_b=lambda x: x + 2, r_b=lambda y: y * 3):
    """
    Генерирует бинарное дерево рекурсивно с использованием кеширования.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: функция для вычисления левой ветви
        r_b: функция для вычисления правой ветви

    Returns:
        Бинарное дерево в виде словаря, или None если высота меньше или равна 0
    """
    if height <= 0:
        return None

    left_tree = gen_bin_tree_recursive(height - 1, l_b(root))
    right_tree = gen_bin_tree_recursive(height - 1, r_b(root))

    return {
        'value': root,
        'left': left_tree,
        'right': right_tree
    }


@lru_cache
def gen_bin_tree_iterative_cache(height=4, root=3, l_b=lambda x: x + 2, r_b=lambda y: y * 3):
    """
    Генерирует бинарное дерево итеративно с использованием кеширования.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: лямбда-функция для вычисления левой ветви
        r_b: лямбда-функция для вычисления правой ветви

    Returns:
        Словарь (dict), или None если высота меньше или равна 0
    """

    if height <= 0:
        return None

    bin_tree = {'value': root, 'left': None, 'right': None}

    line = deque()
    line.append((bin_tree, 1))

    while line:
        current_node, current_level = line.popleft()
        if current_level < height:
            # Левая ветвь
            left_value = l_b(current_node['value'])
            left_node = {'value': left_value, 'left': None, 'right': None}
            current_node['left'] = left_node
            line.append((left_node, current_level + 1))

            # Правая ветвь
            right_value = r_b(current_node['value'])
            right_node = {'value': right_value, 'left': None, 'right': None}
            current_node['right'] = right_node
            line.append((right_node, current_level + 1))

    return bin_tree


def benchmark(func, n, repeat=5):
    """Возвращает среднее время выполнения"""
    times = timeit.repeat(lambda: func(n), number=1, repeat=repeat)
    return min(times)


def main():
    random.seed(42)
    test_data = list(range(0, 10, 2))

    res_recursive = []
    res_iterative = []
    res_recursive_cache = []
    res_iterative_cache = []

    for n in test_data:
        res_recursive.append(benchmark(gen_bin_tree_recursive, n))
        res_iterative.append(benchmark(gen_bin_tree_iterative, n))
        res_recursive_cache.append(benchmark(gen_bin_tree_recursive_cache, n))
        res_iterative_cache.append(benchmark(gen_bin_tree_iterative_cache, n))

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.plot(test_data, res_recursive_cache, label="Рекурсивный с lru_cache")
    plt.plot(test_data, res_iterative_cache, label="Итеративный с lru_cache")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравните время работы двух реализаций функции построения бинарного дерева")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig('binary_tree_comparison.png', dpi=300, bbox_inches='tight')



if __name__ == "__main__":
    main()
