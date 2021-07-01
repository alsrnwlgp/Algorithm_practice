from collections import defaultdict


def dfs(k, v):
    global s, longest, tree, visited, cur
    visited[k] = True
    s.append(k)
    cur += v
    longest = max(cur, longest)
    for nk, nv in tree[k].items():
        if not visited[nk]:
            dfs(nk, nv)
    s.pop()
    cur -= v
            
tree = defaultdict(dict)
N = int(input())
for i in range(1, N+1):
    tmp = list(map(int, input().split()))[1:-1]
    keys = tmp[0::2]
    values = tmp[1::2]
    for k, v in zip(keys, values):
        tree[i][k] = v
s = []
cur = 0
longest = 0
for i in range(1, N+1):
    visited = [False]*(N+1)
    dfs(i, 0)
print(longest)
    