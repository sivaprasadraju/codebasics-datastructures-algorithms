from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is Empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

q = Queue()

def place_order(orders):
    for order in orders:
        print(f"Added the order: {order}")
        q.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        order = q.dequeue()
        print(f"Now serving : {order}")
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()


