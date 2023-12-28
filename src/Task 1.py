# v26

from simplify_to_binary_tree import binary_tree_from_arythmetic_statement


class Node:
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.data = data

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def calculate_down_nodes(self):
        counter = 1
        if self.left:
            if isinstance(self.left, Node):
                counter += self.left.calculate_down_nodes()
            else:
                counter += 1

        if self.right:
            if isinstance(self.right, Node):
                counter += self.right.calculate_down_nodes()
            else:
                counter += 1
        return counter

    def toPrint(self, margin_left: int = 0):
        curr_margin = ''.ljust(margin_left, ' ')
        next_margin_left = margin_left + 3
        add_margin = ''.ljust(next_margin_left, ' ')

        if self.data:
            print(curr_margin, self.data)

        if self.left:
            print(curr_margin, 'Left:')
            if isinstance(self.left, Node):
                self.left.toPrint(next_margin_left)
            else:
                print(add_margin, self.left)

        if self.right:
            print(curr_margin, 'Right:')
            if isinstance(self.right, Node):
                self.right.toPrint(next_margin_left)
            else:
                print(add_margin, self.right)


def arr_to_binary_tree(tree_to_add: list) -> Node:
    if len(tree_to_add) == 3:
        tree = Node(tree_to_add[1])
        if isinstance(tree_to_add[0], list):
            tree.add_left(arr_to_binary_tree(tree_to_add[0]))
        else:
            tree.add_left(tree_to_add[0])
        if isinstance(tree_to_add[2], list):
            tree.add_right(arr_to_binary_tree(tree_to_add[2]))
        else:
            tree.add_right(tree_to_add[2])
        return tree
    else:
        raise TypeError("Not appropriate array")


if __name__ == "__main__":
    expression = "((2+5)×4-7)÷3"
    tree_to_add = binary_tree_from_arythmetic_statement(expression)
    tree = arr_to_binary_tree(tree_to_add)
    tree.toPrint()
    print(''.ljust(60, '-'), '\n',
          f"There's {tree.calculate_down_nodes()} nodes in the binary tree above.")
