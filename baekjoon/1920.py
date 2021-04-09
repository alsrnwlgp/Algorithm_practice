from sys import stdin
read = stdin.readline
N = int(read())
li_1 = list(map(int, read().split()))
M = int(read())
tmp = list(map(int, read().split()))
li_2 = [[dig, i] for i, dig in enumerate(tmp)]
li_1.sort()
li_2.sort()
i = 0
for j, (dig, _) in enumerate(li_2):
    while li_1[i] < dig:
        i += 1
        if i >= N:
            break
    if i >= N:
        for k in range(j, M):
            li_2[k][0] = 0
        break
        
    if li_1[i] == dig:
        li_2[j][0] = 1
    else:
        li_2[j][0] = 0
li_2.sort(key=lambda x: x[1])
for i, _ in li_2:
    print(i)
