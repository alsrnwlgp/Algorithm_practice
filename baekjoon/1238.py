'''
입력된 방향의 반대 방향의 그래프를 만들어 모든 점에서 한점까지 가는데 걸리는
최소한의 시간을 계산
'''
import sys
from sys import stdin
from heapq import heappop, heappush
read = stdin.readline
N, M, X = map(int, read().split())
gph = [[] for _ in range(N+1)]
backgph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2, e = map(int, read().split())
    gph[v1].append((v2, e))
    backgph[v2].append((v1, e))
inf = sys.maxsize
dp = [inf]*(N+1)
backdp = [inf]*(N+1)


def dijkstra(start):
    dp[start] = 0
    h = []
    heappush(h, (0, start))
    while h:
        e, v = heappop(h)
        for nv, ne in gph[v]:
            sume = e + ne
            if sume < dp[nv]:
                dp[nv] = sume
                heappush(h, (sume, nv))
    backdp[start] = 0
    backh = []
    heappush(backh, (0, start))
    while backh:
        e, v = heappop(backh)
        for nv, ne in backgph[v]:
            sume = e + ne
            if sume < backdp[nv]:
                backdp[nv] = sume
                heappush(backh, (sume, nv))


dijkstra(X)
print(max([i+j for i, j in zip(dp[1:], backdp[1:])]))
