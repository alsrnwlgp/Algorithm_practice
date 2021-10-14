def lps(li):
    n = len(li)
    table = [0]*n
    j = 0
    for i in range(1, n):
        while j > 0 and li[i] != li[j]:
            j = table[j-1]
        if li[i] == li[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    ans = 0
    li = []
    n, m = len(s), len(p)
    table = lps(p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans += 1
                li.append(i - m + 2)
                j = table[j]
            else:
                j += 1
    return ans, li


ans, li = kmp(input(), input())
print(ans)
for e in li:
    print(e, end=' ')
