f = open("input.txt", 'r')
read = f.readline
box = []
N = int(read())
for _ in range(N):
    box.append(read().split())
print(box[:4])