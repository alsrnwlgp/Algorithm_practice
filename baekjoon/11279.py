import sys
read = sys.stdin.readline
import heapq

h = []
N = int(read())
for _ in range(N):
    val = int(read())
    if val == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (-val, val))
