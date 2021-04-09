from sys import stdin
read = stdin.readline
N = int(read())
dic = [list(map(int, read()[:-1])) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
ans = []


def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and dic[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if dic[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)
ans.sort()
print(len(ans))
for a in ans:
    print(a)