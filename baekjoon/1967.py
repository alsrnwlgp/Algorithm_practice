# 백준에 소스코드 돌리면 42%에서 런타임 오류남 
# dfs 재귀양에 문제가 있는건가?
from sys import stdin
import sys
sys.setrecursionlimit(10000)
read = stdin.readline
N = int(read())
gph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, read().split())
    gph[a].append((b, c))
    gph[b].append((a, c))


def longest(start):
    _dist = [-1]*(N+1)
    _dist[start] = 0


    def dfs(node):
        for nextn, e in gph[node]:
            if _dist[nextn] == -1:
                _dist[nextn] = _dist[node] + e
                dfs(nextn)


    dfs(start)
    max_dist = max(_dist)
    max_i = _dist.index(max_dist)
    return max_i, max_dist


node, dist = longest(1)
node, dist = longest(node)
print(dist)
