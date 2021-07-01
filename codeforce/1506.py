from sys import stdin
read = stdin.readline
T = int(read())


def test(n, m, x):
    i = x % n - 1
    j = x // n + 1
    return m*i + j
for _ in range(T):
    n, m, x = map(int, read().split())
    print(test(n, m, x))
