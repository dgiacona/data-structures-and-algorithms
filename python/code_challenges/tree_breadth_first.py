from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    tree_breadth = Queue()
    values = []

    if tree.root is None:
        return values

    if not tree_breadth.front:
        tree_breadth.enqueue(tree.root)

    while not tree_breadth.is_empty():

        values.append(tree_breadth.front.value.value)
        front_node = tree_breadth.front.value

        if front_node.left:
            tree_breadth.enqueue(front_node.left)

        if front_node.right:
            tree_breadth.enqueue(front_node.right)

        tree_breadth.dequeue()
        
    return values

