from collections import deque, defaultdict
from copy import deepcopy

N, M = map(int, input().split())
q = deque(list(map(int, input().split()))[1:])
gph = defaultdict(set)
predict = []
for _ in range(M):
    tmp = list(map(int, input().split()))[1:]
    predict.append(tmp)
    for i, a in enumerate(tmp):
        gph[a].update(tmp)
know = [False]*(N+1)
while q:
    for node in deepcopy(q):
        know[node] = True
        for nextn in gph[node]:
            if not know[nextn]:
                q.append(nextn)
        q.popleft()
# know's value 는 진실을 아는지 여부
ans = 0
for e in predict:
    for i in e:
        if know[i]:
            ans -= 1
            break
    ans += 1
print(ans)
