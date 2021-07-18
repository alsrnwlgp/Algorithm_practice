import sys
from collections import deque
MAX = sys.maxsize
read = sys.stdin.readline
n, m = map(int, read().split())
dp = [[MAX]*m for _ in range(n)]
mat = [list(read()[:-1]) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
ones = []
dp[0][0] = 1
q.append((0,0))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dp[nx][ny] != MAX:
                continue
            dp[nx][ny] = dp[x][y] + 1
            if mat[nx][ny] == '0':
                q.append((nx, ny))
            else:
                ones.append((nx, ny))
revq = deque()
revdp = [[MAX]*m for _ in range(n)]
revdp[n-1][m-1] = 1
revq.append((n-1, m-1))
while revq:
    x, y = revq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if revdp[nx][ny] != MAX:
                continue
            revdp[nx][ny] = revdp[x][y] + 1
            if mat[nx][ny] == '0':
                revq.append((nx, ny))
ans = dp[n-1][m-1]
for x, y in ones:
    ans = min(ans, dp[x][y] + revdp[x][y] - 1)
print(ans if ans != MAX else -1)
