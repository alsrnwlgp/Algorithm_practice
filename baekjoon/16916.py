def lps(li):
    n = len(li)
    ans = [0]*n
    j = 0
    for i in range(1, n):
        while j > 0 and li[i] != li[j]:
            j = ans[j-1]
        if li[i] == li[j]:
            j += 1
            ans[i] = j
    return ans


def kmp(s, p):
    n = len(p)
    table = lps(s)
    ans = 0
    j = 0
    for t in s:
        while j>0 and t != p[j]:
            j = table[j-1]
        if t == p[j]:
            if j == n-1:
                ans = 1
                break
            j += 1
    return ans

s, p = input(), input()
print(kmp(s, p))
