'''
pypy로 제출해도 시간초과남....
'''
from sys import stdin
read = stdin.readline


def min_cost(i, j):
    global files, N, dp
    if dp[i][j] != -1:
        return dp[i][j]
    costs = []
    for k in range(i, j):
        costs.append(min_cost(i, k) + min_cost(k+1, j))
    dp[i][j] = min(costs) + sum(files[i:j+1])
    return dp[i][j]

start = time.time()
for _  in range(T):
    N = int(read())
    files = list(map(int, read().split()))
    dp = [[-1]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    print(min_cost(0, N-1))
