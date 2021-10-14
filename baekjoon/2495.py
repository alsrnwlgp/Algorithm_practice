for _ in range(3):
    s = input()
    ans = 1
    res = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans += 1
            res = max(ans, res)
        else:
            ans = 1
    print(res)
