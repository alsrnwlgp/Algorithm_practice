from math import log
n = int(input())
k = int(log(n / 3, 2))
mat = [[' ']*(3*2**(k+1)-1) for _ in range(n)]
dx = [0, 1, 1, 2, 2, 2, 2, 2]
dy = [2, 1, 3, 0, 1, 2, 3, 4]


def make_star(x, y, v):
    if v == 0: 
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            mat[nx][ny] = '*'
        return
    make_star(x, y+2**(v-1)*3, v-1)
    make_star(x+2**(v-1)*3, y, v-1)
    make_star(x+2**(v-1)*3, y+2**(v-1)*6, v-1)


make_star(0,0,k)
for i in range(len(mat)):
    print(''.join(mat[i]))
