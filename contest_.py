n = int(input())

for _ in range(n):
    num = int(input())
    a = num%10
    b = (num - a) // 10
    print(a+b)