# coding=utf-8
# stack的实现包括有 push,pop,peek,isempty,size.

class mystack(object):
    def __init__(self):
        self.stack = []

    def append(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            return 'You are trying to pop item from an empty stack'

    def isempty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.isempty():
            return self.stack[-1]