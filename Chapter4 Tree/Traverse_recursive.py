from collections import deque

def inorder(root):
    if root == None: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if root == None: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if root == None: return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def levelorder(root):
    if root == None: return []
    queue = deque([root])
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res

def level(root):
    if root == None: return []
    queue = deque([root])
    res = []
    while queue:
        next_queue = deque([])
        curr_res = []
        for node in queue:
            curr_res.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
        res.append(curr_res)
    return res

def strucure(root):
    if root == None: return []
    queue = [root]
    res = []
    while queue != len(queue) * [None]:
        next_queue = [None] * (len(queue) * 2)
        curr_res = ['*'] * len(queue)
        for i, node in enumerate(queue):
            if node == None: continue
            next_queue[2 * i] = queue[i].left
            next_queue[2 * i + 1] = queue[i].right
            curr_res[i] = queue[i].val
        res.append(curr_res)
        queue = next_queue
    return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildBST(arr, start, end):
    if start >= end: return None
    if start == end - 1: return TreeNode(arr[start])
    mid = start + (end - start ) / 2
    root = TreeNode(arr[mid])
    root.left = buildBST(arr, start, mid)
    root.right = buildBST(arr, mid + 1, end)
    return root

from random import randint

def main():
    lens = 20
    ans = set()
    for i in xrange(lens):
        ans.add(randint(0, 100))
    arr = sorted(list(ans))
    root = buildBST(arr, 0, len(arr) - 1)
    tree = level(root)
    for l in tree:
        print l

    tree = strucure(root)
    for l in tree:
        print l

    print inorder(root)
    print preorder(root)
    print postorder(root)
    print levelorder(root)



if __name__ == '__main__' :
    main()