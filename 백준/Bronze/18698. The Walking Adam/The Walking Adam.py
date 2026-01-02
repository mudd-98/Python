n = int(input())

for _ in range(n):
    s = list(input())
    cnt = 0

    for c in s:
        if c == 'D':
            break
        else:
            cnt += 1
            
    print(cnt)