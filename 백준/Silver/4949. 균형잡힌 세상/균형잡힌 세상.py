import sys
input = sys.stdin.readline

result = []

while (1):  
  s = input().rstrip()
  if s == '.':
    break

  stk = []
  balanced = True
  
  for c in s:
    if c in '([':
      stk.append(c)
      
    elif c == ')':
      if not stk or stk[-1] != '(':
        balanced = False
        break
      stk.pop()
      
    elif c == ']':
      if not stk or stk[-1] != '[':
        balanced = False
        break
      stk.pop()

  if balanced and not stk:
    result.append('yes')
  else:
    result.append('no')

print('\n'.join(result))