n = int(input())
res = 0

while n != 0:
    if n <= 5:
        res += 1
        n = 0
    if n >5:
        res = n//5
        n =  n%5

print(res)