from collections import deque
from sys import stdin
read = stdin.readline
N = int(read())
gph = [[] for _ in range(N+1)]
for _ in range(1, N+1):
    tmp = list(map(int, read().split()))
    for i in range(1, len(tmp)-2, 2):
        gph[tmp[0]].append((tmp[i], tmp[i+1]))


def bfs(start):
    visit = [-1]*(N+1)
    q = deque()
    q.append(start)
    visit[start] = 0
    max_ = [0, 0]
    while q:
        node = q.popleft()
        for next_node, w in gph[node]:
            if visit[next_node] == -1:
                visit[next_node] = visit[node] + w
                q.append(next_node)
                if max_[1] < visit[next_node]:
                    max_ = next_node, visit[next_node]
    return max_


node, dis = bfs(1)
node, dis = bfs(node)
print(dis)
