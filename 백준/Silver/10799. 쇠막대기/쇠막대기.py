import sys

s = sys.stdin.readline().rstrip()
stk = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stk.append('(')
    else:
        stk.pop()    # 일단 하나를 꺼냄
        
        if s[i-1] == '(':
            ans += len(stk)
        else:
            ans += 1

print(ans)