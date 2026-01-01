n = int(input())

rst = list(map(int, input().split()))

prev = 0
score = 0

for i in rst:
    if i == 1:
        if prev == 0:
            score += 1
            prev += 1
        else:
            score += 1 + prev
            prev += 1
    else:
        prev = 0

print(score)