from sys import stdin, maxsize, stdout
MAX = maxsize
read = stdin.readline
T = int(read())
for _ in range(T):
    n, m, k = map(int, read().split())
    gph = [MAX]*(n+1)
    gph[1] = 0
    edges = []
    for _ in range(m):
        u, v, w = map(int, read().split())
        edges.append((u, v, w))
        edges.append((v, u, w))
    for _ in range(k):
        u, v, w = map(int, read().split())
        edges.append((u, v, -w))
    for _ in range(n-1):
        update = False 
        for u, v, w in edges:
            if gph[v] > gph[u] + w:
                gph[v] = gph[u] + w
                update = True
        if not update:
            break
    # one more edge relaxation - to know whether minus cycle exists or not
    ans = 'NO'
    for u, v, w in edges:
        if gph[v] > gph[u] + w:
            ans = 'YES'
    stdout.write('%s\n'%ans)
