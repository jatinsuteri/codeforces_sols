n = int(input())
count = 0
for _ in range(n):
    x = input()
    if x.count('1') > 1:
        count += 1
print(count)