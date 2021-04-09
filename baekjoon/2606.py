from sys import stdin
read = stdin.readline
dic = dict()
for i in range(int(read())):
    dic[i+1] = set()
for _ in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)
visited = set()


def dfs(start, dic):
    visited.add(start)
    for node in dic[start]:
        if node not in visited:
            dfs(node, dic)


dfs(1, dic)
print(len(visited)-1)
