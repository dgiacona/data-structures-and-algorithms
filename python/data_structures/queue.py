from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Create a Queue:
    front, rear, next
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # method body here
        new_rear = Node(value)
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            old_rear = self.rear
            old_rear.next = new_rear
            self.rear = new_rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        else:
            # remove front
            # reset front
            # return value
            old_front = self.front
            self.front = self.front.next
            return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError()
        return self.front.value

    def is_empty(self):
        if not self.front:
            return True


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
