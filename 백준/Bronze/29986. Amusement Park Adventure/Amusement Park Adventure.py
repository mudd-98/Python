N, H = map(int, input().split())
min_h = list(map(int, input().split()))

cnt = 0
for h in min_h:
  if h <= H:
    cnt += 1

print(cnt)