n = int(input())
for _ in range(n):
    i, s = input().split()
    i = int(i)
    print(s[:i-1] + s[i:])
