n , m , a = map(int, input().split())

len = (n // a) + (1 if n%a != 0 else 0 )
hei = (m // a) + (1 if m%a != 0 else 0 )

print(len*hei)