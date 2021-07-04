inspect = list(input())
explode = list(input())
N, M = len(inspect), len(explode)
s = []
for i, e in enumerate(inspect):
    s.append(e)
    if e == explode[-1]:
        if s[len(s)-M:] == explode:
            for _ in range(M):
                s.pop()
print(''.join(s) if s else 'FRULA')
