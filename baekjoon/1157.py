from collections import defaultdict
s = input()
d = defaultdict(int)
for i in s:
    d[i.upper()] += 1
maxli = []
maxn = 0
for k, v in d.items():
    if v > maxn:
        maxli = [k]
        maxn = v
    elif v == maxn:
        maxli.append(k)
    else:
        continue
print(maxli[0] if len(maxli) == 1 else '?')
