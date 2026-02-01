import sys
input = sys.stdin.readline

n = int(input())
stk = []

for _ in range(n):
  num = int(input())

  if num != 0:
    stk.append(num)
  else:
    stk.pop()

print(sum(stk))