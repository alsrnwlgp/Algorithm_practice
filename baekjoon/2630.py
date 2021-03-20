import sys
read = sys.stdin.readline

def check_box(box):
    first = box[0][0]
    len_box = len(box)
    for i in range(len_box):
        for j in range(len_box):
            if box[i][j] != first:
                a_box = box[:len_box//2]
                box1, box2, box3, box4 = list(), list(), list(), list()
                for e in a_box:
                    box1.append(e[:len_box//2])
                    
                    
                    box2.append(e[len_box//2:])
                b_box = box[len_box//2:]
                for e in b_box:
                    box3.append(e[:len_box//2])
                    box4.append(e[len_box//2:])
                val1 = check_box(box1)
                val2 = check_box(box2)
                val3 = check_box(box3)
                val4 = check_box(box4)
                return val1[0]+val2[0]+val3[0]+val4[0], val1[1]+val2[1]+val3[1]+val4[1]
    return (1, 0) if first == '0' else (0, 1)


N = int(read())
color_map = []
for _ in range(N):
    color_map.append(read().split())
w, b = check_box(color_map)
print(w)
print(b)
