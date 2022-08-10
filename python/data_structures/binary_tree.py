class BinaryTree:
    """
    Put docstring here
    Branch created will revisit this weekend
    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            values.append(root.value)

            walk(root.left)

            walk(root.right)

        walk(self.root)

        return values


    def in_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            walk(root.left)

            values.append(root.value)

            walk(root.right)

        walk(self.root)

        return values

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return

            walk(root.left)

            walk(root.right)

            values.append(root.value)

        walk(self.root)

        return values

    def find_maximum_value(self):
        values = self.post_order()
        max_val = max(values)

        for value in values:
            if value > max_val:
                max_val = value

        return max_val


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
