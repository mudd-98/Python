import sys

l_stk = list(sys.stdin.readline().rstrip())
r_stk = list()

n = int(sys.stdin.readline())

for _ in range(n):
  command = list(sys.stdin.readline().split())

  if command[0] == 'L':
    if l_stk:
      r_stk.append(l_stk.pop())
  elif command[0] == 'D':
    if r_stk:
      l_stk.append(r_stk.pop())
  elif command[0] == 'B':
    if l_stk:
      l_stk.pop()
  else:
    l_stk.append(command[1])

print(''.join(l_stk) + ''.join(reversed(r_stk)))