# dynamic programming with 연쇄행렬 최소곱셈 알고리즘
from sys import stdin
import sys
read = stdin.readline
MAX = sys.maxsize
T = int(read())
for _  in range(T):
    N = int(read())
    files = list(map(int, read().split()))
    dp = [[MAX]*N for _ in range(N)]
    for d in range(0, N):
        for i in range(0, N-d):
            if d == 0:
                dp[i][i+d] = 0
                continue
            j = i + d
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
            dp[i][j] += sum(files[i:j+1])
    print(dp[0][N-1])
