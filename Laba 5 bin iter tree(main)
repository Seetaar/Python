from collections import deque


def gen_bin_tree(height=4, root=12, l_b=lambda x: x ** 3, r_b=lambda y: y * 2 - 1):
    """
    Создает бинарное дерево.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: функция для вычисления левой ветви
        r_b: функция для вычисления правой ветви
    """
    if height <= 0:
        return None
    
    bin_tree = {'root': root, 'left': None, 'right': None}

    if height == 1:
        return bin_tree

    line = deque()
    line.append((bin_tree, 1))

    while line:
        current_node, current_level = line.popleft()

        if current_level >= height:
            continue

        left_value = l_b(current_node['root'])
        right_value = r_b(current_node['root'])

        left_node = {'root': left_value, 'left': None, 'right': None}
        current_node['left'] = left_node
        line.append((left_node, current_level + 1))

        right_node = {'root': right_value, 'left': None, 'right': None}
        current_node['right'] = right_node
        line.append((right_node, current_level + 1))

    return bin_tree


class BinaryTreeVisualizer:
    """
    Класс для визуализации бинарного дерева.
    """

    def __init__(self, tree_dict):
        self.tree = tree_dict

    def display_tree_ascii(self, vis=None, prefix="", is_left=True):
        """Визуализация 1"""
        if vis is None:
            vis = self.tree

        if vis is None:
            return

        if vis.get('right') is not None:
            self.display_tree_ascii(vis['right'], prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(vis['root']))

        if vis.get('left') is not None:
            self.display_tree_ascii(vis['left'], prefix + ("    " if is_left else "│   "), True)

    def display_tree_json(self, tree=None):
        """Визуализация 2"""
        import json
        if tree is None:
            tree = self.tree
        print(json.dumps(tree, indent=2))


if __name__ == "__main__":
    binary_tree = gen_bin_tree(height=4, root=12)
    visualizer = BinaryTreeVisualizer(binary_tree)
    visualizer.display_tree_ascii()
    visualizer.display_tree_json()
