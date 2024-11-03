def solution(p, k, arr):
    res = []
    curr = []
    countp = 0
    def backtrack(i):
        nonlocal res
        nonlocal countp
        if i == len(arr):
            if countp <= k:
                res.append(curr.copy())
            return
        curr.append(arr[i])
        if arr[i] % p == 0: countp += 1
        backtrack(i+1)
        a = curr.pop()
        if a % p == 0: countp -= 1
        backtrack(i+1)
    backtrack(0)
    return len(res) - 1


p , k = map(int , input().split())
arr = list(map(int , input().split()))
print(solution(p, k, arr))

