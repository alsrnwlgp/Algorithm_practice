import sys
sys.setrecursionlimit(10000)
read = sys.stdin.readline

dp = [[[False]*21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif dp[a][b][c] is not False:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


a, b, c = map(int, input().split())
while (a, b, c) != (-1, -1, -1):
    print('w({}, {}, {}) ='.format(a, b, c), w(a, b, c))
    a, b, c = map(int, input().split())
