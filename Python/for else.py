# The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement.

for i in xrange(10):
    continue
else:
    print i
## 9


for i in xrange(10):
    if i == 6:
        print i
        break
else:
    print i
# i = 6

for i in xrange(10):
    continue
print i
# i == 9