import sys

n, m = map(int, input().split())
ans = [0]*m

def make_permutation(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(1, n+1):
        ans[index] = i
        make_permutation(index+1, n, m)
    
make_permutation(0, n, m)