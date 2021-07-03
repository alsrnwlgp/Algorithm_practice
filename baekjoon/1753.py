from sys import stdin
from heapq import heappush, heappop
import sys

read = stdin.readline
inf = sys.maxsize
V, E = map(int, read().split())
start = int(read())
gph = [[] for _ in range(V+1)]
dp = [inf]*(V+1)
for _ in range(E):
    a, b, c = map(int, read().split())
    gph[a].append((c, b))


def dijkstra(start):
    h = []
    dp[start] = 0
    heappush(h, (0, start))
    while h:
        w, v = heappop(h)
        for nw, nv in gph[v]:
            new_w = w + nw
            if new_w < dp[nv]:
                dp[nv] = new_w
                heappush(h, (new_w, nv))


dijkstra(start)
for i in range(1, V+1):
    print(dp[i] if dp[i] < inf else 'INF')
