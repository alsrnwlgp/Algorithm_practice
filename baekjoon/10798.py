li = [input() for _ in range(5)]
maxs = 0
for i in range(5):
    maxs = max(maxs, len(li[i]))
ans = ''
for i in range(maxs):
    for j in range(5):
        if len(li[j]) > i:
            ans += li[j][i]
print(ans)
