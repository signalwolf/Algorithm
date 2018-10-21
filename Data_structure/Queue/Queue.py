# deque: double ended queue

from collections import deque
class Queue(object):
    def __init__(self):
        self.queue = deque()

    def enqueue (self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.popleft()
        else:
            return None

    def isEmpty(self):
        return len(self.queue) == 0
