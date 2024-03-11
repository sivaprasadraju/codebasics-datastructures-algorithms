from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def push(self, val):
        self.container.append(val)

    def size(self):
        return len(self.container)

def reverse_stack(val):
    stack = Stack()
    for ch in val:
        stack.push(ch)

    out = ""

    while stack.size() != 0:
        out += str(stack.pop())

    return out


reversed_string = reverse_stack("We will conquere COVID-19")
print(reversed_string)
