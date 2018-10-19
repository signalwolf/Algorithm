# coding=utf-8

# 在coursra上union find 有两种形式，一个是quick find，一个是quick union。
# quick find 的方法是让建立一个id，让每个node都包含自己的id号码。这样找的时候非常简单，
# 只要比较id是否是一样的就好。但是在union的时候比较慢，O（N2）的时间来union整个list
# 而quick union 的方法则是使用类似tree 的结构，每个node只记住它的parent是谁就好。
# 这样每次查找的时候，需要不断的向上找寻其最后的源头在哪，然后比较源头是否相同。

from random import randint
from collections import defaultdict
def union_find_quick_find (pairs):
    id = {}
    for p, q in pairs:
        pid = id.setdefault(p, p)
        qid = id.setdefault(q, q)
        for i in id.keys():
            if id[i] == pid:
                id[i] = qid
    return id

def root(id, p):
    while id[p] != p:
        p = id[p]
    return p

def union_find_quick_union(pairs):
    id = defaultdict(int)
    for p, q in pairs:
        if p not in id:
            id[p] = p
        if q not in id:
            id[q] = q
        p = root(id, p)
        q = root(id, q)
        id[p] = q
    return id

def find(id, p, q):
    return root(id,p) == root(id,q)

def main():
    n = 10
    pairs = generate(n/2)
    print pairs
    id1 = union_find_quick_find(pairs)
    id2 = union_find_quick_union(pairs)
    print id1
    print id2
    k1, k2 = id1.keys()[0:2]
    print id1[k1] == id1[k2]
    print find(id2, k1, k2)



def generate(n):
    res = set()
    for i in xrange(n):
        first = randint(0, n)
        second = randint(0, n)
        while second == first:
            second = randint(0, n)
        res.add((first, second))
    return res




if __name__ == '__main__':
    main()