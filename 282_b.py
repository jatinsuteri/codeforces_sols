n = int(input())

result = []
total_a = 0
total_g = 0

for _ in range(n):
    ai , gi = map(int, input().split())
    if abs((total_a + ai) - total_g) <= 500:
        result.append("A")
        total_a += ai
    elif abs(total_a - (total_g + gi)) <= 500:
        result.append("G")
        total_g += gi
    else:
        print("-1")
        break
else:
    print(''.join(result))
