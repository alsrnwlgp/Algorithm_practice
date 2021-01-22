import sys
input = sys.stdin.readline

n = int(input())
L = [0 for _ in range(31)]
L[0] = 1
for i in range(1, n+1):
    if i % 2 == 1:
        continue
    j = i
    while j >= 0:
        L[i] += L[j]*2
        j -= 2
    L[i] += L[i-2]
print(L[n])