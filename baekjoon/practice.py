user_id = input()
banned_id = input()

def solution(user_id, banned_id):

    choice_id = [[] for _ in banned_id]
    for i, bi in enumerate(banned_id):
        for ui in user_id:
            if compare_id(ui, bi):
                choice_id[i].append(ui)
    s = []
    l = []
    
    
    def make_possible_id_list(choice_id):
        if not choice_id:
            l.append(s)
        for string in choice_id[0]:
            if string not in s:
                s.append(string)
                make_possible_id_list(choice_id[1:])
                s.pop()
    
    make_possible_id_list(choice_id)
    
    print(l)
    return 0

                
def compare_id(normal_id, star_id):
    if len(normal_id) != len(star_id):
        return False
    for i in range(len(star_id)):
        if star_id[i] == '*':
            continue
        if star_id[i] != normal_id[i]:
            return False
    return True

solution(user_id, banned_id)