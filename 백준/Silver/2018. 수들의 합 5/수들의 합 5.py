import sys

n = int(sys.stdin.readline())

cnt = 0
sum = 0
end = 1

for start in range(1, n+1):
  while sum < n and end <= n:
    sum += end
    end += 1

  if sum == n:
    cnt += 1

  sum -= start

print(cnt)