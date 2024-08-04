n , pos = map(int, input().split())

arr = tuple(map(int, input().split()))

l = r = pos-1
res = 0

if arr[pos-1] == 1:
    res += 1
l-=1
r+=1

while l >= 0 or r < n:
    if l >=0 and r < n:
        if arr[l] == arr[r] == 1:
            res += 2
            
    elif l >= 0:
        if arr[l] == 1:
            res += 1
    
    elif r < n:
        if arr[r] == 1:
            res += 1

    l-=1
    r+=1
    
print(res)