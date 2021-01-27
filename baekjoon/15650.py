import sys
n, m = map(int, input().split())
ans = [0]*m

def make_ascending_permutation(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(ans[index-1]+1, n+1):
        ans[index] = i
        make_ascending_permutation(index+1, n, m)


make_ascending_permutation(0, n, m)