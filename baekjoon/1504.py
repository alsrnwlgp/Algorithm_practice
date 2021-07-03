from sys import stdin
import sys
from heapq import heappush, heappop
read = stdin.readline
inf = sys.maxsize

N, E = map(int, read().split())
gph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, read().split())
    gph[a].append((b,c))
    gph[b].append((a,c))
v1, v2 = map(int, read().split())


def dijkstra(start):
    h = []
    dp = [inf for _ in range(N+1)]
    dp[start] = 0
    heappush(h, (0, start))
    while h:
        w, n = heappop(h)
        for nn, nw in gph[n]:
            if nw + w < dp[nn]:
                dp[nn] = nw + w
                heappush(h, (nw + w, nn))
    return dp


dp1 = dijkstra(1)
dp2 = dijkstra(v1)
dp3 = dijkstra(v2)
result = min(dp1[v1] + dp2[v2] + dp3[N], dp1[v2] + dp3[v1] + dp2[N])
print(result if result < inf else -1)
