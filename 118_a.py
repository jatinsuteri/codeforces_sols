str = input().lower()

res = ""
vowels = ["a", 'e','i','o','u','y']

for i in range(len(str)):
    if str[i] not in vowels:
        res += "." + str[i]

print(res)