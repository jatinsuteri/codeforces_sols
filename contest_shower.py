def solve(t,s,d,res):
    if res[0][0] >= s:
        return "YES"
    
    for i in range(1,t):
        if res[i][0] - res[i-1][1] >= s:
            return "YES"
        
    if d - res[-1][1] >= s:
        return "YES"
    
    return "NO"

days = int(input())

for _ in range(days):
    tasks , showertime, daylen = map(int,input().split())
    res = []
    for _ in range(tasks):
        res.append(list(map(int,input().split())))
    solved = solve(tasks, showertime, daylen,res)
    print(solved)