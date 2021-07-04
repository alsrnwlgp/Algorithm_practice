from sys import stdin
from collections import deque
read = stdin.readline
N = int(read())
gph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, read().split())
    gph[a].append((b, c))
    gph[b].append((a, c))


def bfs(start):
    dist = [-1]*(N+1)
    dist[start] = 0
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for v, e in gph[node]:
            if dist[v] == -1:
                dist[v] = dist[node] + e
                q.append(v)
    max_dist = max(dist)
    max_node = dist.index(max_dist)
    return max_node, max_dist


node, dist = bfs(1)
node, dist = bfs(node)
print(dist)
