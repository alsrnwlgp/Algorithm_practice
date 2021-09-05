from collections import deque


def str_to_list(s):
    if s == '[]':
        return []
    return list(map(int, s[1:-1].split(',')))


def print_list(li):
    print('[', end='')
    for i, e in enumerate(li):
        if i == len(li)-1:
            print(str(e), end='')
        else:
            print(str(e)+',', end='')
    print(']')


T = int(input())
for _ in range(T):
    REVERSE = False
    fs, n, deq = input(), input(), deque(str_to_list(input()))
    error = False
    for f in fs:
        if f == 'R':
            REVERSE = not REVERSE
        elif f == 'D':
            if not deq:
                print('error')
                error = True
                break
            else:
                if REVERSE:
                    deq.pop()
                else:
                    deq.popleft()
    if not error:
        if REVERSE:
            deq.reverse()
        print_list(deq)
