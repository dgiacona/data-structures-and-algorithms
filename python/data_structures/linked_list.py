class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        txt = ""
        current = self.head
        while current:
            txt += f"{{ {current.value} }} -> "
            print(txt)
            current = current.next
        return txt + "NULL"


    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    def insert(self, value):
        # method body here
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
