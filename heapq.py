import heapq
from heapq import *
from random import shuffle

data = range(10)
shuffle(data)
heap=[]
for n in data:
    heappush(heap, n)
heappush(heap, 0.5)



ml = [ mth for mth in dir(heapq) if not mth.startswith('_')]
print("methods:", ml)


