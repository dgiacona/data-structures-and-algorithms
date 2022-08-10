from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        def walk(root, node_to_add):
            if root is None:
                return

            if node_to_add.value < root.value:
                if root.left is None:
                    root.left = node_to_add
                else:
                    walk(root.left, node_to_add)
            else:
                if root.right is None:
                    root.right = node_to_add
                else:
                    walk(root.right, node_to_add)


        walk(self.root, node)

    def contains(self, target):

        def walk(root):
            if root is None:
                return False

            if target == root.value:
                return True

            if target < root.value:
                return walk(root.left)
            else:
                return walk(root.right)

        return walk(self.root)

