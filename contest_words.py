def solve(s, t):
    def is_subsequence(s, t):
        it = iter(s)
        return all(char in it for char in t)

    s_list = list(s)
    t_len = len(t)
    t_index = 0

    for i in range(len(s_list)):
        if s_list[i] == '?':
            if t_index < t_len:
                s_list[i] = t[t_index]
                t_index += 1
            else:
                s_list[i] = 'a'
        elif t_index < t_len and s_list[i] == t[t_index]:
            t_index += 1
    
    modified_s = ''.join(s_list)
    
    if is_subsequence(modified_s, t):
        return "YES", modified_s
    else:
        return "NO"

n = int(input())
res = []
for _ in range(n):
    s = input().strip()
    t = input().strip()
    result = solve(s, t)
    res.append(result)

for result in res:
    if result[0] == "YES":
        print(result[0])
        print(result[1])
    else:
        print(result)
