a = input().lower()
b = input().lower()

t1, t2 = 0 , 0
i = 0

if a == b:
    print(0)

for i in range(len(a)):
    if ord(a[i]) > ord(b[i]):
        print("1")
        break
    elif ord(b[i]) > ord(a[i]):
        print("-1")
        break
    else:
        continue