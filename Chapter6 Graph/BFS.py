
from collections import deque
def mybfs(node, graph):
    queue = deque([])
    # format: curr_node, distance to origianl node
    queue.append([node, 0])
    visited = set([node])
    while queue:
        curr, dis = queue.popleft()
        for ngb in graph[curr]:
            if ngb not in visited:
                visited.add(ngb)
                queue.append([ngb, dis + 1])
    return

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')