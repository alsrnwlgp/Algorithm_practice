import sys
from collections import deque
from collections import defaultdict
import copy


def bfs(man):
    global fgph, N
    result = 0
    visited = [False]*(N+1)
    visited[0] = True
    q = deque()
    q.append(man)
    visited[man] = True
    kb = 1
    while not all(visited):
        for f in copy.deepcopy(q):
            for ff in fgph[f]:
                if not visited[ff]:
                    visited[ff] = True
                    q.append(ff)
            q.popleft()
        result += kb*len(q)
        kb += 1
    return result


N, M = map(int, input().split())
fgph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    fgph[a].append(b)
    fgph[b].append(a)
Minkb = sys.maxsize
ans = 0
for i in range(1, N+1):
    tmp = bfs(i)
    if tmp < Minkb:
        ans = i
        Minkb = tmp
print(ans)
