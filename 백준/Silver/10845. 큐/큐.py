import sys
input = sys.stdin.readline

n = int(input())
stk = []

for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'push':
    stk.append(cmd[1])
  elif cmd[0] == 'pop':
    if len(stk) == 0:
      print(-1)
    else:
      print(stk.pop(0))
  elif cmd[0] == 'size':
    print(len(stk))
  elif cmd[0] == 'empty':
    if len(stk) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'front':
    if len(stk) == 0:
      print(-1)
    else:
      print(stk[0])
  elif cmd[0] == 'back':
    if len(stk) == 0:
      print(-1)
    else:
      print(stk[-1])