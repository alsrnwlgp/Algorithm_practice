def pi(s):
    n = len(s)
    table = [0]*n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    n, m = len(s), len(p)
    table = pi(p)
    ans = 0
    j = 0
    for i in range(n):
        while j>0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans = 1
                break
            j += 1
    return ans


d = '0123456789'
s, p = input(), input()
news = []
for i in s:
    if i not in d:
        news.append(i)
print(kmp(''.join(news), p))
