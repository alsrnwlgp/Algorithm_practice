n, k = int(input()), int(input())
s, e = 1, k
ans = 0
while s <= e:
    mid = (s + e)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    if cnt < k:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid
print(ans)
