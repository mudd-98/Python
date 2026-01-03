n = int(input())

for i in range(1, n):
    print(' ' * (n - i) + '*' * i)

for j in range(0, n):
    print(' ' * j + '*' * (n - j))