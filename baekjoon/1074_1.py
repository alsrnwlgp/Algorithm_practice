def recursion(x, y, N):
    if N == 0:
        return 0
    a = x//(2**(N-1))
    b = y//(2**(N-1))
    if a == 0 and b == 0:
        return recursion(x, y, N-1)
    elif a == 0 and b == 1:
        return 4**(N-1) + recursion(x, y-2**(N-1), N-1)
    elif a == 1 and b == 0:
        return 4**(N-1)*2 + recursion(x-2**(N-1), y, N-1)
    else:
        return 4**(N-1)*3 + recursion(x-2**(N-1), y-2**(N-1), N-1)


N, x, y = map(int, input().split())
print(recursion(x, y, N))
