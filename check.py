from heapq import heappush, heappop, heapify

A = [
    [1, 'k'],
    [1, 'b'],
    [1, 'z'],
    [1, 'd'],
    [2, 'a']
]

heapify(A)

while A:
    print heappop(A)