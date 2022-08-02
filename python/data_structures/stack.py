from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Create a stack:
    Top, next
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):
        # method body here
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            old_top = self.top
            self.top = self.top.next
            return old_top.value

    def is_empty(self):
        if not self.top:
            return True

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
