from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        while self.out_stack.top:
            self.in_stack.push(self.out_stack.pop())
        self.in_stack.push(value)

    def dequeue(self):
        while self.in_stack.top:
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

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
