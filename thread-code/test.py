import gc
n = 1000
a = range(1, n)
a = dict(zip(a, a))
b = []
for k1, v1 in a.iteritems():
   for k2, v2 in a.iteritems():
      b.append((k1,k2))
