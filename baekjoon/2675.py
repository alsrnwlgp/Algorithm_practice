from sys import stdin
read = stdin.readline
N = int(read())
for _ in range(N):
    a, s = read().split()
    a = int(a)
    ans = ''
    for i in range(len(s)):
        ans += s[i]*a
    print(ans)
