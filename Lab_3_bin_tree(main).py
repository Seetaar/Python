def left_branch(root: int) -> int:
    """Левая ветвь"""
    return root ** 3


def right_branch(root: int) -> int:
    """Правая ветвь"""
    return (root * 2) - 1


def gen_bin_tree(height, root, l_b=left_branch, r_b=right_branch):
    """
    Создает бинарное дерево.

    Args:
        height: высота дерева
        root: значение корневого узла
        l_b: функция для вычисления левой ветви
        r_b: функция для вычисления правой ветви
    """
    if height == 0:
        return None

    left_tree = gen_bin_tree(height - 1, l_b(root), l_b, r_b) if height > 1 else None
    right_tree = gen_bin_tree(height - 1, r_b(root), l_b, r_b) if height > 1 else None

    return {
        'root': root,
        'left': left_tree,
        'right': right_tree
    }


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
