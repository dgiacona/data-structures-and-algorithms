from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    tree_breadth = Queue()
    values = []

    if tree.root:
        tree_breadth.enqueue(tree.root)

    if tree.root:
        return values

    while not tree_breadth.is_empty():
        node_front = tree_breadth.front.value


        if node_front.left:
            tree_breadth.enqueue(node_front.left)

        if node_front.right:
            tree_breadth.enqueue(node_front.right)

        values.append(tree_breadth.dequeue().value)

    return values

