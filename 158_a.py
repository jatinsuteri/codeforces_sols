_ , pos = input().split()
pos = int(pos) - 1
arr = input()
arr = arr.split()

kval = arr[pos]

count = 0
for ele in arr:
    if int(ele) > 0 and int(ele) >= int(kval):
        count += 1

print(count)


