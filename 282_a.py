n = int(input())
res = 0

for _ in range(n):
    op = input()
    
    if op[1] == '+':
        res +=1
    elif op[1] == '-':
        res -=1
        
print(res)