from hashlib import md5
val = '10'
m = md5(val)
print m
tmp = m.hexdigest()
print tmp
print type(tmp), len(tmp)
print int(tmp, 16)
print int('10')
print int('10', 10)