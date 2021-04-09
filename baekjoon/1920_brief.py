from sys import stdin
read = stdin.readline
n, S, m = read(), set(read().split()), read()
ans = ''
for i in read().split():
    if i in S:
        ans += '1\n'
    else:
        ans += '0\n'
print(ans)
