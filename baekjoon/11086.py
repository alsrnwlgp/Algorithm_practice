import sys
read = sys.stdin.readline
from collections import deque

T = int(read())
for _ in range(T):
    val = 0
    _ = read()
    li = list(map(int, read().split()))
    li.sort()
    print(li)
    while len(li)>1:
        delta = li[0] + li[1]
        val += delta
        li = li[2:]
        i = 0
        try:
            while li[i]<delta:
                i += 1
            li = li[:i] + [delta] + li[i:]
        except:
            li.append(delta)
        print(li)
    print(val)
    
    