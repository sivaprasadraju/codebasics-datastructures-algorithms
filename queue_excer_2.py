from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def binary_numbers(num):
    q = Queue()
    q.enqueue("1")

    for i in range(num):
        front = q.front()
        print(" ", front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")

        q.dequeue()

binary_numbers(10)
