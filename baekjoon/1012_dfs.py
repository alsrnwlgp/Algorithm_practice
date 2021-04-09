from sys import stdin
import sys
sys.setrecursionlimit(10000)
read = stdin.readline
T = int(read())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, K = map(int, read().split())
    dic = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        ix, iy = map(int, read().split())
        dic[iy][ix] = 1
    cnt = 0


    def dfs(x, y):
        if 0 <= x < M and 0 <= y < N and not visited[y][x] and dic[y][x] == 1:
            visited[y][x] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                dfs(nx, ny)
        pass
    
    
    for y in range(N):
        for x in range(M):
            if dic[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                cnt += 1
    print(cnt)