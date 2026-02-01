import sys
input = sys.stdin.readline

n = int(input())
stk = [0]
next_num = 1
result = []

for _ in range(n):
  num = int(input())

  if stk[-1] > num:
    print('NO')
    exit()
    
  elif stk[-1] == num:
    stk.pop()
    result.append('-')
    
  else:
    while stk[-1] < num:
      stk.append(next_num)
      next_num += 1
      result.append('+')
    stk.pop()
    result.append('-')

print('\n'.join(result))