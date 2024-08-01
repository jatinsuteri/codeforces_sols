arr = []
n = int(input())
for _ in range(n):
    word = input()
    arr.append(word)
 
for i in range(len(arr)):
    word = arr[i]
    if len(word) > 10:
        start = word[0]
        end = word[-1]
        mid = str(len(word) - 2)
        arr[i] = start + mid + end
        
for word in arr:
    print(word)