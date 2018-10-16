# coding=utf-8

# default dict 与 dict 有什么不同
# 1. 对于未在dictionary中的元素的处理，Dict是直接报错，故而我们需要区分在dict中与不在dict中的情况：
dicts = {}
for i in xrange(10):
  if i in dicts:
      dicts[i] += 1
  else:
      dicts[i] = 1
print dicts
# output：
# {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

#   但是对于default dict来说，我们只需要直接先claim它的type，然后再直接添加即可。
from collections import defaultdict
dicts = defaultdict(int)
for i in xrange(10):
    dicts[i] += 1
print dicts

# output:
# defaultdict(<type 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})

#       同样的方法申明还有 int, list, set 等

# 2. default dict 与 dict的不同在于default dict中有一个函数叫做 __missing__(key), 它就是用于处理在dict中要raise error的情况。
# 3. default dict的官方定义：dict subclass that calls a factory function to supply missing values	
