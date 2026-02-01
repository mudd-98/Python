import sys
input = sys.stdin.readline

n = int(input())
stk = []

for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'push':
    stk.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    print(stk.pop() if stk else -1)
  elif cmd[0] == 'size':
    print(len(stk))
  elif cmd[0] == 'empty':
    print(0 if stk else 1)
  elif cmd[0] == 'top':
    print(stk[-1] if stk else -1)