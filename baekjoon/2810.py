def count(s, e):
    ans = 0
    for i in s:
        if i == e:
            ans += 1
    return ans


n = int(input())
s = input()
ans = count(s, 'S') + count(s, 'L')//2 + 1
print(min(ans, n))
