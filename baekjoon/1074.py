import sys


def recursion(x_, y_, N):
    global x, y, ans
    if N == 0:
        if x_ == x and y_ == y:
            print(ans)
            sys.exit(0)
        else:
            ans += 1
        return
    recursion(x_, y_, N-1)
    recursion(x_, y_+2**(N-1), N-1)
    recursion(x_+2**(N-1), y_, N-1)
    recursion(x_+2**(N-1), y_+2**(N-1), N-1)


N, x, y = map(int, input().split())
ans = 0
recursion(0, 0, N)
