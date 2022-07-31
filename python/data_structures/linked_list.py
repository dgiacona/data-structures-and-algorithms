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

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current:
            if not current.next:
                current.next = new_node

                break

            else:
                current = current.next

    def insert_before(self, search_val, value):
        new_node = Node(value)

        if not self.head:
            raise TargetError

        if self.head.value == search_val:
            self.insert(value)
            return

        current = self.head

        while current and current.next:
            if current.next.value == search_val:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next
        raise TargetError

    def insert_after(self, search_val, value):

        current = self.head
        if not self.head:
            raise TargetError

        while current:
            if current.value == search_val:
                self.insert_before(current.next.value, value)
                return
            else:
                current = current.next
        raise TargetError





class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
