from sys import stdin
import sys
from heapq import heappush, heappop
read = stdin.readline
inf = sys.maxsize
N = int(read())
M = int(read())
gph = [[] for _ in range(N+1)]
dp = [inf]*(N+1)
for _ in range(M):
    v1, v2, e = map(int, read().split())
    gph[v1].append((v2, e))


def dijkstra(start):
    h = []
    heappush(h, (0, start))
    dp[start] = 0
    while h:
        e, v = heappop(h)
        for nv, ne in dp[v]:
            sume = e + ne
            if sume < dp[nv]:
                dp[nv] = sume
                heappush((sume, nv))


v1, v2 = map(int, read().split())
dijkstra(v1)
print(dp[v2])
