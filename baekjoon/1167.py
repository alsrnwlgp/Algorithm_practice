'''
모든 노드에서 가장 먼 노드까지의 길이를 구한 알고리즘이다.
시간복잡도가 너무 커서 백준에서 정답으로 인정되지 않는다.
'''
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
    keys, values = tmp[0::2], tmp[1::2]
    for k, v in zip(keys, values):
        tree[i][k] = v
s = []
cur = 0
longest = 0
visited = [False]*(N+1)
for i in range(1, N+1):
    visited = [False]*(N+1)
    longest = 0
    dfs(i, 0)
print(longest)
