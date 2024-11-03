ele = {"A" : 0, "B" : 0,"C" : 0}

for _ in range(3):
    temp = input()
    if temp[1] == ">":
        ele[temp[0]] += 1
    else:
        ele[temp[2]] += 1

res = ""

if ele["A"] == ele["B"] == ele["C"]:
    print("Impossible")

else:
    sorted_ele = sorted(ele.items(), key= lambda x:x[1])
    for a , _ in sorted_ele:
        res += a

    print(res)