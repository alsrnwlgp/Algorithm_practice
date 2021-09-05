import sys
sys.setrecursionlimit(10**8)
tree = []
count = 0
while count <= 10000:
    try:
        tmp = int(input())
    except:
        break
    tree.append(tmp)
    count += 1


def post_order(start, end):
    right = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            right = i
    post_order(start + 1, right - 1)
    post_order(right, end)
    print(start)


post_order(0, len(tree)-1)
