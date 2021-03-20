import sys
read = sys.stdin.readline

N = int(read())
dp = [[0]*41 for _ in range(2)]
dp[0][0], dp[1][1] = 1, 1


def fibonacci(x):
    if dp[0][x] != 0 or dp[1][x] != 0:
        return dp[0][x], dp[1][x]
    dp[0][x], dp[1][x] = fibonacci(x-1)[0] + fibonacci(x-2)[0], fibonacci(x-1)[1] + fibonacci(x-2)[1]
    return dp[0][x], dp[1][x]


for _ in range(N):
    X = int(read())
    print(fibonacci(X)[0], fibonacci(X)[1])
