def solve(i, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = 1 + solve(i // 3, dp)
    return dp[i]

N = 2 * 10**5 + 1
dp = [-1] * (N + 1)

for i in range(N + 1):
    solve(i, dp)

n = int(input())
res = []

for _ in range(n):
    l, r = map(int, input().split())
    
    ans = dp[l] * 2
    for i in range(l + 1, r + 1):
        ans += dp[i]
    
    res.append(ans)

for result in res:
    print(result)
