import sys
read = sys.stdin.readline
M, N = map(int, read().split())
stairs = [list(map(int, read().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if  stairs[nx][ny] < stairs[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0,0))
