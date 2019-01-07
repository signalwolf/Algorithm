from heapq import heappop, heappush
from random import randint
heap = []
for i in xrange(10):
    heappush(heap, (1, randint(1, 10), randint(1, 10)))

while heap:
    print heappop(heap)