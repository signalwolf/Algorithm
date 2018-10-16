# coding=utf-8

dicts = {1:2, 3:4, 5:6}
# method for dicts:
# size of dicts:
print len(dicts)
## output: 3

# delete element:
del dicts[1]
print dicts
## output: {3: 4, 5: 6}

# Clean the dictionary:
dicts.clear()
print dicts
# output: {}

# Copy the dictionary: dicts2 become different dicts:
dicts = {1:2, 3:4, 5:6}
dicts2 = dicts.copy()
print dicts2
## output: {1: 2, 3: 4, 5: 6}
dicts2[3] = 1111
print dicts
## output: {1: 2, 3: 4, 5: 6}
print dicts2
## output: {1: 2, 3: 1111, 5: 6}

# notice the copy is not deep copy, following code changed both dictionary:
dicts = {1:[2,3], 3:[4,5], 4: [6,7]}
dicts2 = dicts.copy()
print dicts
## output:{1: [2, 3], 3: [4, 5], 4: [6, 7]}
dicts2[3][1] = 1111
print dicts2
## output: {1: [2, 3], 3: [4, 1111], 4: [6, 7]}
print dicts
## output: {1: [2, 3], 3: [4, 1111], 4: [6, 7]}

# get all the item in key: value pair (tuple format):
print dicts.items()
## output: [(1, [2, 3]), (3, [4, 1111]), (4, [6, 7])]

# get all the keys:
print dicts.keys()
## output: [1, 3, 4]

#get all the values:
print dicts.values()
## output: [[2, 3], [4, 1111], [6, 7]]

# get specified value and if not found, return some value
print dicts.get(3, 100)
## [4, 1111]
print dicts.get(100, 100)
## 100
print dicts
## {1: [2, 3], 3: [4, 1111], 4: [6, 7]}

# get specified value and if not found, add default value into dicts:
print dicts.setdefault(3, 100)
## [4, 1111]
print dicts.setdefault(100, 100)
## 100
print dicts
## {1: [2, 3], 3: [4, 1111], 4: [6, 7], 100: 100}

# merge two dicts, but seems only work for int, list is not working.
x = {'a':1, 'b': 2}
y = {'b':1, 'c': 11}
x.update(y)
print x