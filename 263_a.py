mat = []
for i in range(5):
    a = []
    a = list(map(int , input().split()))
    mat.append(a)
    
a , b = 0 , 0 

for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            a , b = i , j

print(abs(a-2) + abs(b-2))
